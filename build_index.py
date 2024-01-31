import os

from tqdm import tqdm

import chromadb
from crawl import fetch_urls, find_pages
from parse import get_entries


def main(temp_dir: str, chroma_persist_dir: str, chroma_collection_name: str):
    pages = find_pages()

    fetch_urls(pages, directory=temp_dir, replace=False)

    entries = []
    for file in tqdm(os.listdir(temp_dir), desc="Parsing documentation"):
        with open(os.path.join(temp_dir, file), 'r') as f:
            html = f.read()
            entries.extend(get_entries(html))

    print("Calculating embeddings...")
    client = chromadb.PersistentClient(path=chroma_persist_dir)
    collection = client.get_or_create_collection(name = chroma_collection_name)
    collection.add(
        ids=[str(i) for i in range(len(entries))],
        documents=entries
    )
    print(f"Finished building index with {len(entries)} embeddings")


if __name__ == "__main__":
    import argparse

    TEMP_DIR = 'temp/'
    CHROMA_PERSIST_DIR = 'chromadb/'
    CHROMA_COLLECTION = 'racket'

    # Create the parser
    parser = argparse.ArgumentParser(description="Set search engine params")

    # Add the arguments
    parser.add_argument('--chroma-dir', type=str, help='the directory for ChromaDB', default=CHROMA_PERSIST_DIR)
    parser.add_argument('--collection', type=str, help='the collection for ChromaDB', default=CHROMA_COLLECTION)
    parser.add_argument('--temp-dir', type=str, help='the directory for temp HTML', default=TEMP_DIR)

    # Parse the arguments
    args = parser.parse_args()

    main(chroma_persist_dir=args.chroma_dir, chroma_collection_name=args.collection, temp_dir=args.temp_dir)

