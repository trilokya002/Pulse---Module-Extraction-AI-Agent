import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from urllib.parse import urljoin, urlparse
from collections import deque

HEADERS = {"User-Agent": "Mozilla/5.0"}

def crawl_site(start_url, max_pages=30):
    visited = set()
    queue = deque([start_url])
    documents = []

    base_domain = urlparse(start_url).netloc

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "lxml")
            documents.append({
                "url": url,
                "html": soup
            })

            visited.add(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                parsed = urlparse(full_url)

                if parsed.netloc == base_domain and full_url not in visited:
                    queue.append(full_url)

        except Exception:
            continue

    return documents
