from sentence_transformers import SentenceTransformer

class EmbeddingsCreator:
    def __init__(self, modelo="all-MiniLM-L6-v2"):
        self.modelo = SentenceTransformer(modelo)

    def crear_embeddings(self, chunks):
        embeddings = []

        for i, chunk in enumerate(chunks):
            vector = self.modelo.encode(chunk)
            embeddings.append({
                "chunk": chunk,
                "embedding": vector
            })

        return embeddings
