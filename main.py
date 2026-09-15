from enrichment.parser import parse_website
from enrichment.website import fetch_website
from input.url_input import get_company_url
from models.company import Company
from validation.domain import extract_domain
from validation.technologies import detect_technologies
from validation.url_validator import validate_url


def main():
    url = get_company_url()

    if not validate_url(url):
        print("Invalid URL")
        return

    company = Company(url)

    company.domain = extract_domain(url)

    print(f"Received valid URL: {company.url}")
    print(f"Domain: {company.domain}")

    result = fetch_website(company.url)

    if not result["success"]:
        print(f"Website fetch failed: {result['error']}")
        return

    html = result["html"]

    print(f"Downloaded: {len(html)} bytes")

    page = parse_website(html)

    company.name = page["title"]
    company.description = page["text"]

    company.technologies = detect_technologies(html)

    print(f"Title: {company.name}")
    print(f"Text: {company.description}")
    print(f"Technologies: {company.technologies}")


if __name__ == "__main__":
    main()