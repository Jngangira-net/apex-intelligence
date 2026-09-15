from enrichment.parser import parse_website
from enrichment.website import fetch_website
from input.url_input import get_company_url
from validation.domain import extract_domain
from validation.url_validator import validate_url


def main():
    url = get_company_url()

    if not validate_url(url):
        print("Invalid URL")
        return

    domain = extract_domain(url)

    print(f"Received valid URL: {url}")
    print(f"Domain: {domain}")


    html = fetch_website(url)

    print(f"Downloaded: {len(html)} bytes")

    page = parse_website(html)

    print(f"Title: {page['title']}")
    print(f"Text: {page['text']}")

if __name__ == "__main__":
    main()