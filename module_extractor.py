import argparse
from crawler import crawl_site
from inference_engine import infer_modules
from utils import is_valid_url
import json

def extract_modules(urls):
    all_docs = []
    for url in urls:
        if not is_valid_url(url):
            print(f"Invalid URL skipped: {url}")
            continue
        all_docs.extend(crawl_site(url))

    return infer_modules(all_docs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pulse Module Extraction AI Agent")
    parser.add_argument(
        "--urls",
        nargs="+",
        required=True,
        help="Documentation URLs"
    )

    args = parser.parse_args()
    result = extract_modules(args.urls)

    print(json.dumps(result, indent=2))
