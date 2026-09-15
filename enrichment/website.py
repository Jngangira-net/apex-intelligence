from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def fetch_website(url):
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    try:
        response = urlopen(request, timeout=10)
        return {
            "success": True,
            "status": response.status,
            "html": response.read(),
            "error": None
        }

    except HTTPError as error:
        return {
            "success": False,
            "status": error.code,
            "html": b"",
            "error": f"HTTP {error.code}"
        }

    except URLError as error:
        return {
            "success": False,
            "status": None,
            "html": b"",
            "error": str(error.reason)
        }