from parse import get_entries
from crawl import find_pages, fetch_urls

import os

pages = find_pages()

temp_dir = 'temp/'
fetch_urls(pages, directory=temp_dir, replace=False)

entries = []
for file in os.listdir(temp_dir):
    with open(os.path.join(temp_dir, file), 'r') as f:
        html = f.read()
        entries.extend(get_entries(html))

for entry in entries:
    print(entry)
    break