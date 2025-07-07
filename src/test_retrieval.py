from rag_retriever import load_retriever, retrieve_top_k_chunks

collection = load_retriever()

question = "How are credit card complaints usually handled?"
top_chunks = retrieve_top_k_chunks(question, collection)

for i, (doc, meta) in enumerate(top_chunks):
    print(f"--- Result {i+1} ---")
    print(f"Product: {meta['product']}")
    print(doc)
    print()
