import chromadb

CHROMA_PERSIST_DIR = 'chromadb/'
CHROMA_COLLECTION = 'racket'
k = 1


client = chromadb.PersistentClient(path=CHROMA_PERSIST_DIR)
collection = client.get_or_create_collection(name = CHROMA_COLLECTION)

while True:
    query = input("> ")
    response = collection.query(query_texts=[query], n_results=k)
    docs = response['documents'][0]
    for doc in docs:
        print(doc)
        print('-' * 30)