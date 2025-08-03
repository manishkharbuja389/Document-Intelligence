from sentence_transformers import SentenceTransformer
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def embed_chunks(chunks):
    return model.encode(chunks, show_progress_bar=True)