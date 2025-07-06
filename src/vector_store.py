import chromadb
import pandas as pd
import os
from sentence_transformers import SentenceTransformer
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from tqdm import tqdm

def create_chroma_vector_store(df, persist_path="vector_store/", batch_size=5000):
    os.makedirs(persist_path, exist_ok=True)

    client = chromadb.PersistentClient(path=persist_path)
    embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    collection = client.get_or_create_collection(
        name="complaints",
        embedding_function=embedding_function
    )

    print(f"🧠 Total documents to embed: {len(df)}")
    
    for i in tqdm(range(0, len(df), batch_size), desc="🔄 Adding to ChromaDB"):
        batch = df.iloc[i:i+batch_size]
        collection.add(
            documents=batch['text_chunk'].tolist(),
            metadatas=batch[['complaint_id', 'product']].to_dict(orient='records'),
            ids=[str(idx) for idx in batch.index]
        )

    print("✅ ChromaDB vector store created and persisted.")



if __name__ == "__main__":
    df = pd.read_parquet(r"C:\10x AIMastery\rag-financial-feedback\data\processed\embedded_chunks.parquet")
    create_chroma_vector_store(df)