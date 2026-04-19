import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
from collections import deque


class Crawler:
    def __init__(self, seed_url, max_pages=50):
        self.max_pages = max_pages
        self.visited = set()
        self.documents = []

        # handle single OR multiple seeds
        if isinstance(seed_url, list):
            self.queue = deque(seed_url)
            self.base_domains = [urlparse(url).netloc for url in seed_url]
        else:
            self.queue = deque([seed_url])
            self.base_domains = [urlparse(seed_url).netloc]

        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; IRIS/1.0)"
        }

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=5)

            if response.status_code == 200:
                return response.text
            else:
                print(f"Blocked: {url} ({response.status_code})")

        except Exception as e:
            print(f"Error: {url} -> {e}")

        return None

    def extract_text(self, html):
        soup = BeautifulSoup(html, "lxml")

        # remove unwanted tags (expanded cleanup)
        for tag in soup([
            "script", "style", "noscript",
            "header", "footer", "nav", "aside"
        ]):
            tag.decompose()

        # remove wikipedia-specific junk
        for tag in soup.select(".mw-editsection, .reference, .reflist"):
            tag.decompose()

        text = soup.get_text(separator=" ")
        return " ".join(text.split())

    def extract_links(self, html, base_url):
        soup = BeautifulSoup(html, "lxml")
        links = set()

        for tag in soup.find_all("a", href=True):
            href = tag["href"]
            full_url = urljoin(base_url, href)

            parsed = urlparse(full_url)

            # only http(s)
            if parsed.scheme not in ["http", "https"]:
                continue

            # stay within allowed domains
            if not any(domain in parsed.netloc for domain in self.base_domains):
                continue

            # remove fragment (#section)
            clean_url = full_url.split("#")[0]

            if any(x in clean_url for x in [
                "action=",
                "edit",
                "Special:",
                "Wikipedia:",
                "File:",
                "Help:",
                "Category:",
                "Portal:",
                "Talk:",
                "Template:",
                "w/index.php"
            ]):
                continue

            links.add(clean_url)

        return links

    def crawl(self):
        doc_id = 0

        while self.queue and len(self.visited) < self.max_pages:
            url = self.queue.popleft()

            if url in self.visited:
                continue

            print(f"Crawling: {url}")

            html = self.fetch_page(url)
            if not html:
                continue

            text = self.extract_text(html)

            self.documents.append({
                "id": doc_id,
                "url": url,
                "text": text
            })

            self.visited.add(url)
            doc_id += 1

            # extract and enqueue links
            links = self.extract_links(html, url)
            print(f"→ Found {len(links)} links")

            for link in links:
                if link not in self.visited:
                    self.queue.append(link)

        return self.documents

    def save(self, path="storage/documents.json"):
        with open(path, "w") as f:
            json.dump(self.documents, f, indent=2)

        print(f"Saved {len(self.documents)} documents → {path}")