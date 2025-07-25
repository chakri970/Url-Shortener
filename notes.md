# NOTES.md

## Project: URL Shortener Service

### Implementation Approach

- Developed a Flask-based REST API for URL shortening with in-memory storage.
- Implemented three main endpoints:
  - `POST /api/shorten` to generate a 6-character alphanumeric short code for valid URLs.
  - `GET /<short_code>` to redirect to the original URL while tracking click counts.
  - `GET /api/stats/<short_code>` to return analytics including total clicks and creation timestamp.
- Used thread-safe locking to handle concurrent access to the in-memory URL store.
- Validated URLs using Python’s `urllib.parse` to ensure only proper HTTP/HTTPS URLs are shortened.
- Incorporated basic error handling and meaningful HTTP response codes.
- Wrote pytest test cases covering key functionality and edge cases.

## AI Tools Used
- **ChatGPT (OpenAI)**: Assisted in generating initial code structure, Flask routes, utility functions, and documentation drafts.
- **GitHub Copilot**: Provided code suggestions and completion mainly for repetitive parts like validation and testing.

## Usage

- **Project Planning & Breakdown**: Used to understand the assignment, design endpoints (`/api/shorten`, `/short_code`, `/api/stats/<short_code>`), and outline the folder structure.
- **Code Generation Support**:
  - Initial draft of `main.py`, including Flask route structure.
  - Helped write helper functions (e.g., `generate_short_code`, `validate_url`).
  - Assisted in writing test cases for core functionality using `pytest`.
- **Bug Fixes & Debugging**: Used to troubleshoot `ValueError`, threading issues, and Flask route redirection behavior.
- **Documentation**:
  - Helped write the `README.md` and `NOTES.md` files.
  - Suggested formatting for API usage examples and curl commands.

## AI-Generated Code Review

- Most AI-suggested code was **modified** to fit the exact assignment spec.
- Short code generation logic was inspired by AI, but adjusted to handle collision checks.
- Validation logic was adapted and simplified from AI suggestion.
- Custom error messages and return formats were manually fine-tuned.
  
## Purpose of AI Assistance
- Accelerate boilerplate code writing.
- Suggest best practices for API design and error handling.
- Help draft professional README and NOTES files.
- Generate test templates covering core and edge cases.

## Personal Contributions
- Reviewed and refactored all AI-generated code to ensure correctness, readability, and alignment with requirements.
- Implemented thread-safe in-memory storage for concurrency.
- Enhanced error handling and validation beyond AI suggestions.
- Developed and passed comprehensive unit tests.
- Manually wrote detailed setup, usage instructions, and project structure documentation.
- Ensured clean code and maintainable project architecture.

## Approach Summary
- Focused on core URL shortening logic first.
- Used Python’s built-in data structures for simplicity and performance.
- Designed short codes as random 6-character alphanumeric strings.
- Ensured safe handling of concurrent requests with thread locks.
- Prioritized functionality, robustness, and clear API responses.

## Additional Notes
- The project uses in-memory storage, so data resets on server restart by design.
- AI was used as a tool, not a replacement for understanding or coding.
- This submission reflects my capability to integrate AI assistance responsibly while delivering a quality software solution.

---

Thank you for reviewing my submission. I am happy to discuss any part of the project or my approach during interviews.