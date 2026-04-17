from crawler.crawler import Crawler

if __name__ == "__main__":
    seed = [
    "https://en.wikipedia.org/wiki/Information_retrieval",
    "https://en.wikipedia.org/wiki/Machine_learning",
    "https://en.wikipedia.org/wiki/Data_mining"
    ]
    crawler = Crawler(seed_url=seed, max_pages=30)

    docs = crawler.crawl()
    crawler.save()

    print(f"Crawled {len(docs)} pages")