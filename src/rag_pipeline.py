from rag_retriever import load_retriever, retrieve_top_k_chunks
from rag_generator import generate_answer

def run_rag_pipeline(question, k=5):
    collection = load_retriever()
    results = retrieve_top_k_chunks(question, collection, k=k)

    if not results:  # 🛑 check if results is empty
        return {
            "question": question,
            "answer": "I'm sorry, I couldn't find relevant information in the complaint data to answer that.",
            "sources": [],
            "metadata": []
        }

    # ✅ Only run zip if results exist
    context_chunks, metadatas = zip(*results)

    answer = generate_answer(question, context_chunks)

    return {
        "question": question,
        "answer": answer,
        "sources": context_chunks[:2],  # show top 2 sources
        "metadata": metadatas[:2]
    }
