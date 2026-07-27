# Descripción del proyecto
Este proyecto implementa Pipo, un agente de inteligencia artificial basado en RAG (Retrieval-Augmented Generation) que permite a cualquier persona colaboradora hacer preguntas y recibir respuestas contextualizadas sobre la Escuela de Yoga Luz del Prana.
El sistema carga un PDF, lo divide en fragmentos, genera embeddings, los almacena en FAISS y utiliza un modelo local de Ollama para responder preguntas con contexto.

## Tecnologías utilizadas
- Python 3.11

- FastAPI

- Uvicorn

- FAISS (CPU)

- SentenceTransformers

- pypdf

- Ollama


Ejemplo:



## 🎯 Objetivo del proyecto
El objetivo de este proyecto es simplificar el acceso a la información y evitar que las personas colaboradoras tengan que abrir múltiples archivos y documentos para resolver sus dudas.  
Pipo centraliza todo el conocimiento en un solo punto, ofreciendo respuestas rápidas, claras y contextualizadas.
