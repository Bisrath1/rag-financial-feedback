# # src/data_processing.py

import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_data(path):
    df = pd.read_csv(path)
    return df

def chunk_narratives(df, column='cleaned_narrative', chunk_size=300, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    all_chunks = []
    
    for i, row in df.iterrows():
        chunks = text_splitter.split_text(row[column])
        for chunk in chunks:
            all_chunks.append({
                'complaint_id': i,
                'product': row['Product'],
                'text_chunk': chunk
            })
    return pd.DataFrame(all_chunks)



if __name__ == "__main__":
    df = load_data('data/processed/filtered_complaints.csv')
    chunks_df = chunk_narratives(df)
    print(chunks_df.head())
    chunks_df.to_csv('data/processed/chunks.csv', index=False)



from sentence_transformers import SentenceTransformer
import numpy as np
import os

def embed_chunks(chunks_df, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks_df['text_chunk'].tolist(), show_progress_bar=True)
    chunks_df['embedding'] = embeddings.tolist()
    return chunks_df


if __name__ == "__main__":
    df = load_data('data/processed/filtered_complaints.csv')
    chunks_df = chunk_narratives(df)
    chunks_df = embed_chunks(chunks_df)
    chunks_df.to_parquet('data/processed/embedded_chunks.parquet', index=False)
