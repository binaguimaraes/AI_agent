# 🧘‍♂️ Descripción del proyecto
Este proyecto implementa Pipo, un agente de inteligencia artificial basado en RAG (Retrieval-Augmented Generation) que permite a cualquier persona colaboradora hacer preguntas y recibir respuestas contextualizadas sobre la Escuela de Yoga Luz del Prana.

## 🔐 API Key de OpenAI

Este proyecto está desplegado en la nube mediante Oracle Cloud Infrastructure (OCI). Las personas colaboradoras envían preguntas a través del endpoint público de la API.

Ejemplo:

```
POST http://TU-IP-PUBLICA:8000/pipo
{
  "texto": "Hola Pipo, ¿qué es yoga?"
}
```

La API utiliza la API key configurada en el servidor para generar la respuesta.

## 🎯 Objetivo del proyecto
El objetivo de este proyecto es simplificar el acceso a la información y evitar que las personas colaboradoras tengan que abrir múltiples archivos y documentos para resolver sus dudas.  
Pipo centraliza todo el conocimiento en un solo punto, ofreciendo respuestas rápidas, claras y contextualizadas.
