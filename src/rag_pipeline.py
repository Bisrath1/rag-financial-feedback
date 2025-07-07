from rag_retriever import load_retriever, retrieve_top_k_chunks
from rag_generator import generate_answer

def run_rag_pipeline(question, k=5):
    collection = load_retriever()
    results = retrieve_top_k_chunks(question, collection, k=k)
    
    # Unzip
    context_chunks, metadatas = zip(*results)
    
    answer = generate_answer(question, context_chunks)
    
    return {
        "question": question,
        "answer": answer,
        "sources": context_chunks[:2],  # show 2 most relevant chunks
        "metadata": metadatas[:2]
    }
