import requests
from bs4 import BeautifulSoup

SECTIONS = [
    "https://www.bbc.com/news",
    "https://www.bbc.com/news/world",
    "https://www.bbc.com/news/business",
    "https://www.bbc.com/news/technology",
    "https://www.bbc.com/news/science_and_environment"
]

def scrape_bbc():
    articles_data = []
    seen_titles = set()

    for url in SECTIONS:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for article in soup.find_all("div", {"data-testid": "edinburgh-card"}):
            title_tag = article.find("h2", {"data-testid": "card-headline"})
            title = title_tag.text.strip() if title_tag else "No title available"

            if title in seen_titles:
                continue
            seen_titles.add(title)

            description_tag = article.find("p", {"data-testid": "card-description"})
            description = description_tag.text.strip() if description_tag else "No description available"

            link_tag = article.find("a", {"data-testid": "internal-link"})
            link = "No link available"
            if link_tag:
                link = link_tag.get("href", "No link available")
                if link and not link.startswith("http"):
                    link = "https://www.bbc.com" + link

            category_tag = article.find("span", {"data-testid": "card-metadata-tag"})
            category = category_tag.text.strip() if category_tag else "Unknown category"

            time_tag = article.find("time")
            time_published = time_tag.text.strip() if time_tag else "Unknown time"

            img_tag = article.find("img")
            img_src = img_tag["src"] if img_tag else "No image available"

            articles_data.append({
                "title": title,
                "description": description,
                "link": link,
                "category": category,
                "time_published": time_published,
                "image": img_src
            })

    return articles_data
