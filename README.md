# Url-Shortener
# URL Shortener Service

## Overview

This project implements a lightweight URL shortening service, similar to popular tools like TinyURL or Bitly. It transforms lengthy, unwieldy URLs into concise, easy-to-share short links. The service seamlessly redirects users from these short URLs to their original destinations while tracking usage statistics such as click counts. Designed with simplicity and efficiency in mind, it provides essential URL shortening functionality with fast, thread-safe in-memory storage and clear API responses.

---

## Features

- Generate 6-character alphanumeric short codes for long URLs  
- Redirect users from the short URL to the original URL seamlessly  
- Keep track of how many times each short URL is used  
- Provide an analytics endpoint with useful info like the original URL, number of clicks, and when it was created  
- Validate URLs to make sure only real HTTP or HTTPS addresses get shortened  
- Thread-safe in-memory storage to handle multiple users at once  
- Clean error handling with clear responses  
- Unit tests to ensure everything works and edge cases are covered  

---

## Getting Started

### What You’ll Need

- Python 3.8 or newer  
- `pip` package manager (comes with Python)

### Quick Setup Guide

```bash
# Clone the repository to your local machine
git clone <your_repo_url>
cd url-shortener
```
## (Optional but recommended) Create and activate a virtual environment
```bash
python -m venv venv
```

## Windows users:
```bash
venv\Scripts\activate
```

## macOS/Linux users:
```bash
source venv/bin/activate
```

## Install the required Python packages
```bash
pip install -r requirements.txt
```

## Tell Flask which app to run (PowerShell example)
```bash
$env:FLASK_APP = "app.main"
```

## Start the Flask development server
```bash
python -m flask run
```

## Your API will be available at http://localhost:5000
# How to Use the API

## Shorten a URL
Send a POST request to /api/shorten with JSON body:

``` json

{ "url": "https://your-long-url.com/path" }
```
You will receive a JSON response containing a short_code and a full short_url.

## Redirect
Access the short URL in your browser or via curl:

``` arduino

http://localhost:5000/<short_code>
```
This will redirect you to the original URL.

## Get Analytics
Send a GET request to /api/stats/<short_code> to get statistics:

- Original URL

- Total click count

- Creation timestamp

Example response:

```json

{
  "url": "https://your-long-url.com/path",
  "clicks": 10,
  "created_at": "2024-01-01T10:00:00Z"
}
```
## Limitations & Future Improvements
- Data Persistence: Currently uses in-memory storage, so all data is lost on server restart.
  Future: Integrate a persistent database like SQLite, PostgreSQL, or Redis.

- Rate Limiting & Abuse Prevention: No mechanisms to limit requests or prevent spam/abuse.
  Future: Add rate limiting, CAPTCHA, or authentication.

- Custom Short Codes: Users cannot specify their own short codes.
  Future: Allow custom aliases with validation.

- Scalability: Single-instance, not designed for distributed environments.
  Future: Add distributed caching and database, containerization, and load balancing.

- No User Accounts: No authentication or user management.
  Future: Add user accounts for personalized link management.
# Testing
Run automated tests to verify functionality:

```bash
pytest
```
# Notes
This project relies on in-memory storage, which means all shortened URLs and their data will be lost whenever the server restarts. 
It’s intentionally designed this way to keep the focus on core URL shortening functionality without the complexity of external databases or user authentication.

If you have any questions or need assistance, don’t hesitate to reach out — I’m happy to help!



