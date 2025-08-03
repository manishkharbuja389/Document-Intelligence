import faiss
import numpy as np
import pickle

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.vectors = []
        self.metadata = []

    def add(self, embeddings, metas):
        self.index.add(np.array(embeddings).astype(np.float32))
        self.metadata.extend(metas)

    def search(self, query_vector, k=5):
        D, I = self.index.search(np.array([query_vector]).astype(np.float32), k)
        return [
            {"meta": self.metadata[i], "score": float(D[0][j])}
            for j, i in enumerate(I[0]) if i < len(self.metadata)
        ]

    def save(self, index_path, meta_path):
        faiss.write_index(self.index, index_path)
        with open(meta_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, index_path, meta_path="meta.pkl"):
        self.index = faiss.read_index(index_path)
        try:
            with open(meta_path, "rb") as f:
                self.metadata = pickle.load(f)
        except FileNotFoundError:
            self.metadata = []
