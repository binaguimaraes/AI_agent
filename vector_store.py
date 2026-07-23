import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks = []

    def agregar_embeddings(self, embeddings):
        vectores = []
        for item in embeddings:
            vectores.append(item["embedding"])
            self.chunks.append(item["chunk"])

        vectores_np = np.array(vectores).astype("float32")
        self.index.add(vectores_np)

    def buscar(self, consulta_vector, k=3):
        consulta_np = np.array([consulta_vector]).astype("float32")
        distancias, indices = self.index.search(consulta_np, k)

        resultados = []
        for idx in indices[0]:
            resultados.append(self.chunks[idx])

        return resultados
