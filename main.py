import chromadb
from rag import rag
import sys

use_rag = '-r' in sys.argv or '--rag' in sys.argv

CHROMA_PERSIST_DIR = 'chromadb/'
CHROMA_COLLECTION = 'racket'
k = 5


client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
collection = client.get_or_create_collection(name = CHROMA_COLLECTION)

while True:
    query = input("> ")
    response = collection.query(query_texts=[query], n_results=k)

    if use_rag:
        print(rag(prompt=query, result=response))
    else:
        docs = response['documents'][0]
        for doc in docs:
            print(doc)
    print('-' * 30)