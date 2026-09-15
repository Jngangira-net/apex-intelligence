def extract_identity(page):
    title = page["title"]
    text = page["text"]

    name = title

    if ":" in name:
        name = name.split(":", 1)[0]

    if " - " in name:
        name = name.split(" - ", 1)[0]

    return {
        "name": name.strip(),
        "description": text[:500]
    }