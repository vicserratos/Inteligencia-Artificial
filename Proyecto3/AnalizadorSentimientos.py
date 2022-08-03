from CargaDatos import CargaDatos
from Entrenamiento import Entrenamiento
from CalculaSentimiento import CalculaSentimiento
from ApiTwitter import ApiTwitter
from Tokenizer import Tokenizer

class AnalizadorSentimientos:

    def menu():
        print("¿Que deseas hacer?")
        print("\ta. Entrenar un modelo nuevo\n")
        print("\tb. Calcular sentimientos (Ya tienes un modelo entrenado)")
    
        op = input("Ingresa a o b:  ")
        if(op != "a"):
            if(op != "b"):
                return 0        
        return op

    def subMenu():
        #tamanioSet = 30
        #porcentajeEntrenamiento = 0.7
        #iteraciones = 15
        #excluirSubSet = .1
        print("\nDefine los siguientes valores: ")
        print("\tTamaño del conjunto de entrenamiento")
        tamanioSet = input("Ingresa número natural:  ")
        print("\tPorcentaje del tamaño del conjunto de entrenamiento")
        porcentajeEntrenamiento = input("Ingresa número entre 0 y 1:  ")
        print("\tIteraciones de entrenamiento")
        iteraciones = input("Ingresa número natural:  ")
        print("\tDel subconjunto obtenido de entrenamiento da un porcentaje que quieres utilizar")
        excluirSubSet = input("Ingresa número entre 0 y 1:  ")
        return [tamanioSet, porcentajeEntrenamiento, iteraciones, excluirSubSet]

    def getSentimiento():
        print("\nVamos a cualcular un sentimiento")
        tweet = input("Introduce tu tweet: ")

        print("\nEjemplo de Tokenizer")
        t = Tokenizer()
        t.ejemplo(tweet)

        print("\nCalculando sentimiento")
        cs = CalculaSentimiento()      
        cs.getSentimiento(tweet)

    if __name__ == "__main__":
        #palabrasClave = ['covid','coronavirus', 'lang:en']
        #a = ApiTwitter()
        #a.inicalizaStremTwitter(palabrasClave)
        opcion = menu()
        if(opcion == "a"):
            resultados = subMenu()
            tamanioSet = int(resultados[0])
            porcentajeEntrenamiento = float(resultados[1])
            iteraciones = int(resultados[2])
            excluirSubSet = float(resultados[3])

            cargaDatos = CargaDatos()
            print("Cargando datos\n")
            print("El tamaño definido es: ", str(tamanioSet))
            print("Porcentaje de set entrenamiento: ", str(porcentajeEntrenamiento))
            print("Porcentaje tamaño set prueba: ", str( -round(porcentajeEntrenamiento - 1, 1) ))
            print()
            setEntrenamiento, setTest = cargaDatos.cargaDatosEntrenamiento(tamanioSet, porcentajeEntrenamiento)
            
            entrenamiento = Entrenamiento()
            print("Generando modelo de entrenamiento\n")
            entrenamiento.entrenaModelo(setEntrenamiento, setTest, iteraciones, excluirSubSet)
            print("\n¡¡¡ Fin del entrenamiento !!!")
            getSentimiento()

        if(opcion == "b"):
            getSentimiento()
