def display_company_report(company, downloaded_bytes):
    print()
    print("=" * 60)
    print("                 APEX INTELLIGENCE")
    print("              COMPANY INTELLIGENCE")
    print("=" * 60)

    print()
    print("COMPANY")
    print("-" * 60)
    print(f"Name        : {company.name}")
    print(f"Domain      : {company.domain}")
    print(f"Industry    : {company.industry}")
    print(f"URL         : {company.url}")

    print()
    print("WEBSITE")
    print("-" * 60)
    print("Status      : Online")
    print(f"Downloaded  : {downloaded_bytes} bytes")

    print()
    print("TECHNOLOGIES")
    print("-" * 60)

    if company.technologies:
        for finding in company.technologies:
            print(f"[+] {finding['technology']}")
            print(f"    Evidence : {finding['evidence']}")
    else:
        print("No technology fingerprints detected.")

    print()
    print("=" * 60)