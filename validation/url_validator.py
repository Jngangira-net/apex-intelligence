from urllib.parse import urlparse


def validate_url(url):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        return False

    return bool(parsed.netloc)