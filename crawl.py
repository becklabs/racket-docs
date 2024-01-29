import os
from typing import List

import requests
from bs4 import BeautifulSoup


def find_pages(index_url: str ="https://docs.racket-lang.org/reference/") -> List[str]:
    """
    Find all urls that point to doc pages on the given index page 
    """
    data = requests.get(index_url, timeout=5)
    soup = BeautifulSoup(data.content, "html.parser")

    # Find all <a> tags
    links = soup.find_all('a')

    # Extract the URLs from the href attribute
    urls = list(set([link.get('href') for link in links if link.get('href') is not None]))
    filtered_urls = [url for url in urls if url.endswith('.html') and not url.startswith('../')]
    absolute_urls = [f'{index_url}{url}' for url in filtered_urls]
    return absolute_urls

def fetch_urls(urls: List[str], directory: str, replace: bool = True) -> None:
    """
    Save each URL as an HTML file in the directory. 
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:
        name = url.split('/')[-1]
        path = f"{directory}/{name}"
        if not replace and os.path.exists(path):
            continue
        response = requests.get(url, timeout=5)
        with open(path, "w") as file:
            file.write(response.text)

if __name__ == "__main__":
    pages = find_pages()
    fetch_urls(pages, directory='temp/')

