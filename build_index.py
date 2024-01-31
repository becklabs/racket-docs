import os

from tqdm import tqdm

import chromadb
from crawl import fetch_urls, find_pages
from parse import get_entries

TEMP_DIR = 'temp/'
CHROMA_PERSIST_DIR = 'chromadb/'
CHROMA_COLLECTION = 'racket'

pages = find_pages()

fetch_urls(pages, directory=TEMP_DIR, replace=False)

entries = []
for file in tqdm(os.listdir(TEMP_DIR), desc="Parsing documentation"):
    with open(os.path.join(TEMP_DIR, file), 'r') as f:
        html = f.read()
        entries.extend(get_entries(html))

print("Calculating embeddings...")
client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
collection = client.get_or_create_collection(name = CHROMA_COLLECTION)
collection.add(
    ids=[str(i) for i in range(len(entries))],
    documents=entries
)
print(f"Finished building index with {len(entries)} embeddings")

