from input.url_input import get_company_url


def main():
    url = get_company_url()
    print(f'Received: {url}')


if __name__ == "__main__":
    main()