import chromadb
from rag import rag

CHROMA_PERSIST_DIR = 'chromadb/'
CHROMA_COLLECTION = 'racket'
k = 10


client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
collection = client.get_or_create_collection(name = CHROMA_COLLECTION)

while True:
    query = input("> ")
    response = collection.query(query_texts=[query], n_results=k)

    print(rag(prompt=query, result=response))
    print('-' * 30)
    # docs = response['documents'][0]
    # for doc in docs:
    #     print(doc)
    #     print('-' * 30)