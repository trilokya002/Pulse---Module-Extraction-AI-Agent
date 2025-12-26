def extract_structured_content(soup):
    content = []
    current_section = None

    for tag in soup.find_all(["h1", "h2", "h3", "p", "li"]):
        text = tag.get_text(strip=True)
        if not text:
            continue

        if tag.name in ["h1", "h2"]:
            current_section = text
            content.append({
                "section": current_section,
                "text": ""
            })
        elif current_section:
            content[-1]["text"] += " " + text

    return content
