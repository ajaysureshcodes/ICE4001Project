import requests
from bs4 import BeautifulSoup
import re

def is_malayalam(text):
    # Malayalam Unicode range: 0D00–0D7F
    return bool(re.search(r'[\u0D00-\u0D7F]', text))

def extract_malayalam_text(url):
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, 'html.parser')
        texts = []
        for tag in soup.find_all(['p', 'span', 'div']):
            txt = tag.get_text(separator=' ', strip=True)
            if is_malayalam(txt):
                texts.append(txt)
        return '\n'.join(texts)
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

if __name__ == "__main__":
    # Example Malayalam news URLs
    urls = [
        "https://www.manoramaonline.com/news/latest-news.html",
        "https://www.mathrubhumi.com/news/kerala",
        "https://www.malayalamexpressnews.com/"
    ]
    for url in urls:
        print(f"Scraping: {url}")
        mal_text = extract_malayalam_text(url)
        if mal_text:
            with open("malayalam_news.txt", "a", encoding="utf-8") as f:
                f.write(f"\n--- Content from {url} ---\n")
                f.write(mal_text + "\n")
        else:
            print(f"No Malayalam text found in {url}")