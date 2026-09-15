from urllib.request import urlopen


def fetch_website(url):
    response = urlopen(url, timeout=10)
    html = response.read()

    return html