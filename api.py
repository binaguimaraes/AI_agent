from fastapi import FastAPI
from pydantic import BaseModel

from loader import PDFLoader
from chunker import Chunker
from embeddings import EmbeddingsCreator
from vector_store import VectorStore
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Pergunta(BaseModel):
    texto: str

@app.post("/pipo")
def pipo_endpoint(pergunta: Pergunta):
    loader = PDFLoader("./data/documento.pdf")
    texto = loader.load()

    chunker = Chunker(tamano_chunk=800, solapamiento=200)
    chunks = chunker.dividir(texto)

    creator = EmbeddingsCreator()
    embeddings = creator.crear_embeddings(chunks)

    dimension = len(embeddings[0]["embedding"])
    store = VectorStore(dimension)
    store.agregar_embeddings(embeddings)

    consulta_vector = creator.modelo.encode(pergunta.texto)
    resultados = store.buscar(consulta_vector, k=3)

    contexto = "\n\n".join(resultados)

    prompt = f"""
Eres Pipo, un guía de yoga amable y consciente.
Responde en español, con claridad y calma.

Documento (contexto relevante):
{contexto}

Pregunta del usuario:
{pergunta.texto}
"""

    completion = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    resposta = completion.output[0].content[0].text
    return {"respuesta": resposta}
