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
<img width="1689" height="740" alt="Screenshot 2026-07-27 030858" src="https://github.com/user-attachments/assets/3d1364d5-142d-4f40-962e-1fc6d301dc49" />
<img width="1529" height="205" alt="Screenshot 2026-07-27 030815" src="https://github.com/user-attachments/assets/ee175541-636d-4dcb-bdff-02ce9e423acf" />

<img width="1669" height="748" alt="image" src="https://github.com/user-attachments/assets/eaddd733-9824-456a-958b-94ffa4632296" />
<img width="1542" height="373" alt="image" src="https://github.com/user-attachments/assets/79ab3fb1-0a8e-4bf8-81ac-34b83bc959d2" />



## 🎯 Objetivo del proyecto
El objetivo de este proyecto es simplificar el acceso a la información y evitar que las personas colaboradoras tengan que abrir múltiples archivos y documentos para resolver sus dudas.  
Pipo centraliza todo el conocimiento en un solo punto, ofreciendo respuestas rápidas, claras y contextualizadas.
