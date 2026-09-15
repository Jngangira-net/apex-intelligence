from input.url_input import get_company_url
from validation.url_validator import validate_url
from validation.domain import extract_domain


def main():
    url = get_company_url()

    if not validate_url(url):
        print("Invalid URL")
        return

    domain = extract_domain(url)

    print(f"Received valid URL: {url}")
    print(f"Domain: {domain}")


if __name__ == "__main__":
    main()