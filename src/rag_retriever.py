import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def load_retriever(persist_path="vector_store/", collection_name="complaints"):
    # Load the persisted ChromaDB client
    client = chromadb.PersistentClient(path=persist_path)

    # Use same embedding model from Task 2
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    # Load the collection
    collection = client.get_collection(name=collection_name, embedding_function=embedding_function)

    return collection

def retrieve_top_k_chunks(question, collection, k=5):
    results = collection.query(
        query_texts=[question],
        n_results=k
    )

    # Flatten the results
    documents = results['documents'][0]
    metadatas = results['metadatas'][0]

    return list(zip(documents, metadatas))
