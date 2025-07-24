# TODO: Implement utility functions here
# Consider functions for:
# - Generating short codes
# - Validating URLs
# - Any other helper functions you need

from urllib.parse import urlparse
import string
import random


def is_valid_url(url):
    try:
        parsed = urlparse(url)

        return parsed.scheme in ("http", "https") and bool(parsed.netloc)

    except Exception:
        return False


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
