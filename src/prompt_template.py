def format_prompt(question, context_chunks):
    context_text = "\n---\n".join(context_chunks)
    
    prompt = f"""
You are a financial analyst assistant for CrediTrust.
Your task is to answer questions about customer complaints.

Use the following retrieved complaint excerpts to formulate your answer. 
If the context doesn't contain the answer, state that you don't have enough information.

Context:
{context_text}

Question: {question}
Answer:
    """
    return prompt.strip()
