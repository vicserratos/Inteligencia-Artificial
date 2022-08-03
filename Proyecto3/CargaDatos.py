import os
import random

class CargaDatos():

    # Se cargan los datos de entrenamiento y prueba se etiquetan y se dividen en dos partes
    # porcentajeEntrenamiento es el tamaño del subconjuto de entrenamiento en porcentaje, el valor dado es de entrenamiento y el restante es de prueba
    # TamanioSet es el tamaño del set de entrenamiento que vamos a tomar, entre mas grande mas tiempo toma.
    def cargaDatosEntrenamiento(self, tamanioSet, porcentajeEntrenamiento):
        path = "data/entrenamiento"
        textos = []

        for etiqueta in ["pos", "neg"]:
            pathTexto = path + "/" + etiqueta
            self.auxCargaDatosEntrenamiento(pathTexto, textos, etiqueta)   
        random.shuffle(textos)

        if tamanioSet:
            textos = textos[:tamanioSet]
        porcentajeEntrenamiento = int(len(textos) * porcentajeEntrenamiento)
        return textos[:porcentajeEntrenamiento], textos[porcentajeEntrenamiento:]

    # Carga y etiqueta los textos asiganndo una categoria dentro de spacy
    def auxCargaDatosEntrenamiento(self, pathTexto, textos, etiqueta):
        for archivoTexto in os.listdir(pathTexto):
            with open(f"{pathTexto}/{archivoTexto}") as f:
                texto = f.read()
                texto = texto.replace("<br />", "\n\n")
                #print(texto)
                if texto.strip():
                    spacy_cats = { "cats": {
                                            "pos" : "pos" == etiqueta,
                                            "neg" : "neg" == etiqueta,
                                            }
                    }
                    textos.append((texto, spacy_cats))
