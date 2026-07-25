import os
from pypdf import PdfReader

class PDFLoader:
    def __init__(self, camino_pdf: str):
        self.camino_pdf = camino_pdf
        self.texto = ""
        print(f"[LOG] Loader inicializado para el archivo: {self.camino_pdf}")

    def verificar_existencia(self):
        print("[LOG] Verificando la existencia del archivo...")
        if not os.path.exists(self.camino_pdf):
            raise FileNotFoundError(f"[ERROR] Archivo no encontrado: {self.camino_pdf}")
        print("[LOG] Archivo encontrado con éxito.")

    def cargar_documento(self):
        try:
            reader = PdfReader(self.camino_pdf)
            return reader
        except Exception as e:
            raise RuntimeError(f"[ERROR] Fallo al abrir el archivo PDF: {e}")

    def extraer_texto(self, reader):
        texto_total = ""

        for i, pagina in enumerate(reader.pages):
            contenido = pagina.extract_text()
            if contenido:
                texto_total += contenido + "\n\n"
            else:
                print(f"[AVISO] La página {i+1} está vacía o no contiene texto seleccionable.")

        self.texto = texto_total

    def limpiar_texto(self):
        texto_limpio = (
            self.texto.replace("\n\n\n", "\n\n")
                       .replace("  ", " ")
                       .strip()
        )
        self.texto = texto_limpio

    def load(self) -> str:
        self.verificar_existencia()
        reader = self.cargar_documento()
        self.extraer_texto(reader)
        self.limpiar_texto()
        return self.texto