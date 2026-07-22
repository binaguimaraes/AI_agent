from loader import PDFLoader
from chunker import Chunker
from embeddings import EmbeddingsCreator
from vector_store import VectorStore

loader = PDFLoader("./data/documento.pdf")
texto = loader.load()
chunker = Chunker(tamano_chunk=800, solapamiento=200)
chunks = chunker.dividir(texto)
creator = EmbeddingsCreator()
embeddings = creator.crear_embeddings(chunks)
dimension = len(embeddings[0]["embedding"])
store = VectorStore(dimension)
store.agregar_embeddings(embeddings)
consulta = "precio de la formación de profesores"
consulta_vector = creator.modelo.encode(consulta)
resultados = store.buscar(consulta_vector, k=3)

for r in resultados:
    print("----")
    print(r)