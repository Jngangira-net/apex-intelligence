from html.parser import HTMLParser


class WebsiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.text = []
        self.in_title = False
        self.ignore_content = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True

        if tag in ("style", "script", "noscript"):
            self.ignore_content = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

        if tag in ("style", "script", "noscript"):
            self.ignore_content = False

    def handle_data(self, data):
        if self.ignore_content:
            return

        text = data.strip()

        if not text:
            return

        if self.in_title:
            self.title += text
        else:
            self.text.append(text)


def parse_website(html):
    parser = WebsiteParser()
    parser.feed(html.decode("utf-8", errors="ignore"))

    return {
        "title": parser.title,
        "text": " ".join(parser.text)
    }