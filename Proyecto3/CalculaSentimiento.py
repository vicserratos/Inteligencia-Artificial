import spacy

# Ejecuta el modelo generado y spacy calcula el sentimiento del tweet
class CalculaSentimiento:

    def getSentimiento(self, texto):
        modelo = spacy.load("modeloData")
        # Entrega el analisis
        analisis = modelo(texto)
        # De acuerdo al analisi se obtiene el valor que se daria como "positivo" y el "negativo", de acuerdo a eso se obtiene el sentimiento y el score
        #print(analisis.cats["pos"])
        #print(analisis.cats["neg"])
        if analisis.cats["pos"] > analisis.cats["neg"]:
            calculo = "Positivo :)"
            score = analisis.cats["pos"]
        else:
            calculo = "Negativo :("
            score = analisis.cats["neg"]
        print("Tweet: ", texto, "\n", "Sentimiento calculado: ", calculo, "\t", "Score: ", score)
