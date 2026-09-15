from enrichment.identity import extract_identity
from enrichment.industry import detect_industry
from enrichment.parser import parse_website
from enrichment.website import fetch_website
from input.url_input import get_company_url
from models.company import Company
from output.console_report import display_company_report
from validation.domain import extract_domain
from validation.technologies import detect_technologies
from validation.url_validator import validate_url


def main():
    # Get company URL
    url = get_company_url()

    # Validate URL
    if not validate_url(url):
        print("Invalid URL")
        return

    # Create company object
    company = Company(url)

    # Extract domain
    company.domain = extract_domain(url)

    # Fetch website
    result = fetch_website(company.url)

    if not result["success"]:
        print(f"Website fetch failed: {result['error']}")
        return

    html = result["html"]

    # Parse website content
    page = parse_website(html)

    identity = extract_identity(page)
    company.name = identity["name"]
    company.description = identity["description"]

    industry = detect_industry(page["text"])
    company.industry = industry["industry"]

    # Detect technologies
    company.technologies = detect_technologies(html)

    # Present final report
    display_company_report(company, len(html))


if __name__ == "__main__":
    main()