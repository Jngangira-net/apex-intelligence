def detect_technologies(html):
    html_text = html.decode("utf-8", errors="ignore").lower()

    fingerprints = {
        "WordPress": ["wp-content", "wp-includes"],
        "Shopify": ["cdn.shopify.com"],
        "React": ["_reactroot", "react-dom"],
        "Next.js": ["_next/static", "__next_f"],
        "Vue.js": ["vue.js"],
        "Google Analytics": ["google-analytics.com", "gtag("],
        "Cloudflare": ["cloudflare"],
    }

    findings = []

    for technology, indicators in fingerprints.items():
        for indicator in indicators:
            if indicator in html_text:
                findings.append({
                    "technology": technology,
                    "evidence": indicator
                })
                break

    return findings