from flask import request, jsonify, redirect, abort
from app import app
from app import models
from app import utils

# Health check endpoint for root URL
# Returns a simple JSON indicating the service is up and running


@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

# Additional health check endpoint for API monitoring


@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

# Endpoint to shorten a long URL
# Accepts POST requests with JSON body containing a "url" field
# Validates the URL, generates a unique 6-character short code,
# stores the mapping. Returns the short code and a full shortened URL


@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    # Check if 'url' key is present in the JSON body
    if not data or 'url' not in data:
        return jsonify({"error": "Missing URL"}), 400

    url = data['url']

    # Validate URL format using helper function
    if not utils.is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    # Try generating a unique short code, up to 5 attempts to avoid collisions
    for _ in range(5):
        short_code = utils.generate_short_code()
        # Check if this short code is already used
        if not models.get_url(short_code):
            # Save the mapping of short code to original URL
            models.add_url(short_code, url)
            # Construct the full short URL for user
            short_url = request.host_url + short_code
            return jsonify({"short_code": short_code, "short_url": short_url})

    # If unable to generate a unique code after retries, return error
    return jsonify({"error": "Could not generate unique code"}), 500

# Redirect endpoint to use short URLs
# Given a short code, redirect user to the original URL
# If short code does not exist, return 404 error
# Each redirect increments the click count for analytics


@app.route('/<short_code>')
def redirect_short_url(short_code):
    info = models.get_url(short_code)
    if not info:
        abort(404)
    # Increment click count safely
    models.increment_click(short_code)
    # Redirect with HTTP status 302 (Found)
    return redirect(info['url'], code=302)

# Analytics endpoint to get stats for a short code
# Returns JSON with original URL, number of clicks, and creation timestamp


@app.route('/api/stats/<short_code>')
def stats(short_code):
    info = models.get_stats(short_code)
    if not info:
        abort(404)
    return jsonify({
        "url": info['url'],
        "clicks": info['clicks'],
        # Format datetime in ISO 8601 with trailing 'Z' for UTC time
        "created_at": info['created_at'].isoformat() + "Z"
    })

# Run the Flask development server if this script is executed directly


if __name__ == "__main__":
    # Host 0.0.0.0 makes it accessible from other machines in the network
    # Debug=True enables hot reload
    # and provides better error messages during development
    app.run(host='0.0.0.0', port=5000, debug=True)
