import chromadb


def main(chroma_persist_dir: str, chroma_collection_name: str, top_k: int):
    client = chromadb.PersistentClient(path=chroma_persist_dir)
    collection = client.get_or_create_collection(name = chroma_collection_name)

    while True:
        query = input("> ")
        response = collection.query(query_texts=[query], n_results=top_k)
        docs = response['documents'][0]
        for doc in docs:
            print(doc)
            print('-' * 30)

if __name__ == "__main__":
    import argparse

    CHROMA_PERSIST_DIR = 'chromadb/'
    CHROMA_COLLECTION = 'racket'
    TOP_K = 1

    # Create the parser
    parser = argparse.ArgumentParser(description="Set search engine params")

    # Add the arguments
    parser.add_argument('--dir', type=str, help='the directory for ChromaDB', default=CHROMA_PERSIST_DIR)
    parser.add_argument('--collection', type=str, help='the collection for ChromaDB', default=CHROMA_COLLECTION)
    parser.add_argument('--n-results', type=int, help='the number of results', default=TOP_K)

    # Parse the arguments
    args = parser.parse_args()

    main(chroma_persist_dir=args.dir, chroma_collection_name=args.collection, top_k=args.n_results)