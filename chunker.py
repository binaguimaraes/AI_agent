class Chunker:
    def __init__(self, tamano_chunk=800, solapamiento=200):
        self.tamano_chunk = tamano_chunk
        self.solapamiento = solapamiento

    def dividir(self, texto: str):
        chunks = []
        inicio = 0
        longitud = len(texto)

        while inicio < longitud:
            fin = inicio + self.tamano_chunk
            chunk = texto[inicio:fin].strip()

            if chunk:
                chunks.append(chunk)

            inicio = fin - self.solapamiento

        return chunks


