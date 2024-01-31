import ollama
from chromadb import QueryResult

def rag(prompt: str, result: QueryResult, model='codellama:7b'):
    get_model(model)

    context = [{ 'role': 'system', 'content': 'You are a code assistant designed to answer questions about the Racket programming language. \
                Use the context from the Racket docs provided to answer the prompt.'}]
    [context.append({ 'role': 'assistant', 'content': str(document)}) for document in result['documents']]
    
    context.append({ 'role': 'user', 'content': prompt})  

    response = ollama.chat(model=model, messages=context)

    return response['message']['content']

def get_model(model='codellama:7b'):
    try:
        ollama.show(model)
    except ollama.ResponseError as e:
        if e.status_code == 404:
            print(f'Model {model} not found, trying to pull...') 
            ollama.pull(model)

