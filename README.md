# 🧠 Intelligent Complaint Analysis for Financial Services

This project is part of the **iCog Labs AI Mastery Internship Program**. It leverages **Retrieval-Augmented Generation (RAG)** to build a question-answering system over real financial complaints from the CFPB dataset.

---

## 📌 Overview

This system allows users to ask natural language questions about financial issues. It retrieves relevant customer complaint narratives and uses a language model to generate helpful, grounded answers.

---

## 🔧 Features

- ✅ Cleaned and filtered CFPB complaint dataset  
- ✅ Text chunking of narratives for better semantic understanding  
- ✅ Vector embedding using `sentence-transformers/all-MiniLM-L6-v2`  
- ✅ Vector store built using ChromaDB  
- ✅ Retrieval and answer generation pipeline (RAG)  
- ✅ Interactive chatbot interface with Streamlit  
- ✅ Source transparency – shows which complaint excerpts were used

---

## 📂 Project Structure

```
📁 data/
├── filtered_complaints.csv
├── processed/
└── vector_store/

📁 notebooks/
├── 1.0-eda.ipynb
└── 2.0-embedding.ipynb

📁 src/
├── eda_preprocessing.py
├── chunk_embed_index.py
├── vector_store.py
└── rag_pipeline.py

📁 app/
└── app.py

📄 requirements.txt
📄 README.md
```

---

## 🚀 How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the chatbot interface**
   ```bash
   streamlit run app/app.py
   ```

3. **Try asking questions like:**
   - "What are the most common complaints about personal loans?"
   - "Are savings accounts often closed without notice?"
   - "Is there a delay in Buy Now Pay Later refunds?"

---

## 🧠 Model Used

We use [`all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) because:

- It’s lightweight and fast for real-time semantic search
- Performs well on similarity and retrieval tasks
- Open-source (Apache 2.0) and easy to integrate

---

## 📊 Evaluation

We evaluated the system using 5–10 financial queries. Each response was analyzed based on:

- Quality of the retrieved sources
- Faithfulness and relevance of the generated answer
- Clarity of the final response

A full evaluation table is included in the project report.

---



---

## 📬 Contact

**Bisrat Haile**  
📧 bisrathaile1919@gmail.com  
📍 Addis Ababa, Ethiopia

---

## 📝 License

This project is licensed under the **MIT License**.
