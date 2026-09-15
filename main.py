from input.url_input import get_company_url
from validation.url_validator import validate_url


def main():
    url = get_company_url()


    if validate_url(url):
        print(f'Received valid URL: {url}')
    else:
        print("Invalid URL provided.")


if __name__ == "__main__":
    main()