if __name__ == "__main__":
    df = pd.read_parquet("data/processed/embedded_chunks.parquet")
    create_chroma_vector_store(df)