from fastapi import FastAPI
from pydantic import BaseModel
from loader import PDFLoader
from chunker import Chunker
from embeddings import EmbeddingsCreator
from vector_store import VectorStore
import os
import requests

app = FastAPI()

PDF_PATH = "./data/documento.pdf"

print("Iniciando...")
loader = PDFLoader(PDF_PATH)
texto = loader.load()
chunker = Chunker(tamano_chunk=800, solapamiento=200)
chunks = chunker.dividir(texto)
creator = EmbeddingsCreator()
embeddings = creator.crear_embeddings(chunks)
dimension = len(embeddings[0]["embedding"])
store = VectorStore(dimension)
store.agregar_embeddings(embeddings)

print("Listo!")

def consultar_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",   
            "prompt": prompt,
            "stream": False 
        }
    )

    data = response.json()

    if "response" in data:
        return data["response"]
    else:
        return f"Erro no modelo: {data}"

class Pregunta(BaseModel):
    texto: str

@app.post("/pipo")
def pipo_endpoint(pregunta: Pregunta):

    consulta_vector = creator.modelo.encode(pregunta.texto)
    resultados = store.buscar(consulta_vector, k=3)

    contexto = "\n\n".join(resultados)

    prompt = f"""
Eres Pipo, un guía de yoga amable y consciente.
Responde en español, con claridad y calma.

Documento (contexto relevante):
{contexto}

Pregunta del usuario:
{pregunta.texto}
"""

    respuesta = consultar_ollama(prompt)
    respuesta = str(respuesta).replace("\n", " ")

    return {"respuesta": respuesta}

