import random
import spacy
import en_core_web_sm

class Entrenamiento:
    
    def entrenaModelo(self, setEntrenamiento, setTest, iteraciones, excluirSubSet):
        # textcat() es un categorizador de texto, sobre un texto dado realiza la clasificación sobre un texto.
        # Se le proporcionan etiquetas, de la cual sólo le corre´ponde una a cada texto
        # Proporciona varias arquitecturas y utilizamos una red neuronal conculacional (CNN) ya predefinida
        nlp = en_core_web_sm.load()
        textcat = nlp.create_pipe( "textcat", config={"architecture": "simple_cnn"})
        nlp.add_pipe(textcat)
        textcat.add_label("pos")
        textcat.add_label("neg")
        
        # Se ejecuta sólo texcat y no otros modelos
        pipesSinTextcat = nlp.pipe_names
        pipesSinTextcat.remove('textcat')

        with nlp.disable_pipes(pipesSinTextcat):

            # Regresa una función optimizadora la cual nos sirve para actualizar los pesos en el modelo
            funOptimizadora = nlp.begin_training()
            #Excluye en porcentaje un subconjunto de conjunto de entrenamiento, esto permite que no sea el mismo entrenamiento en las pasadas

            # Se generan "n" entrenamientos
            for i in range(iteraciones):
                print("Entrenamiento #: ", str(i))
                perdidas = {}
                random.shuffle(setEntrenamiento)
                for dato in setEntrenamiento:
                    tweet, etiquetas = zip(dato)
                    # print(tweet, etiquetas)
                    # Actualiza los pesos del modelo
                    nlp.update(tweet, etiquetas, excluirSubSet, funOptimizadora, perdidas)
                with textcat.model.use_params(funOptimizadora.averages):
                    resultados = self.evaluaModelo(nlp.tokenizer, textcat, setTest)
                print("Prueba del modelo")
                print("Gradiente de Perdida \tCalculo \tRecall \tF-score")
                print(perdidas['textcat'], "\t", resultados['calculo'], "\t", resultados['recall'], "\t", resultados['f-score'])
                print()
        # Se guarda el modelo para no hacer el calculo cada ejecución
        with nlp.use_params(funOptimizadora.averages):
            nlp.to_disk("modeloData")

    # Evalua el modelo
    # El calculo es que tan preciso fue ser un verdadero positivo
    # Es la proporcion de verdaderos positivos
    # F-score es el rendimeinto de la funcion
    def evaluaModelo(self, tokenizer, textcat, setTest) -> dict:
        tweets, etiquetas = zip(*setTest)
        tweets = (tokenizer(tweet) for tweet in tweets)
        positivosVerdaderos = 0
        falsosPositivos = 1e-8  
        negativosVerdaderos = 0
        falsosNegativos = 1e-8
        for i, tweet in enumerate(textcat.pipe(tweets)):
            etiquetaCat = etiquetas[i]["cats"]
            for prediccion, score in tweet.cats.items():
                if prediccion == "neg":
                    continue
                if score >= 0.5 and etiquetaCat["pos"]:
                    positivosVerdaderos += 1
                elif score >= 0.5 and etiquetaCat["neg"]:
                    falsosPositivos += 1
                elif score < 0.5 and etiquetaCat["neg"]:
                    negativosVerdaderos += 1
                elif score < 0.5 and etiquetaCat["pos"]:
                    falsosNegativos += 1
        calculo = positivosVerdaderos / (positivosVerdaderos + falsosPositivos)
        recall = positivosVerdaderos / (positivosVerdaderos + falsosNegativos)

        if calculo + recall == 0:
            f_score = 0
        else:
            f_score = 2 * (calculo * recall) / (calculo + recall)
        return {"calculo": calculo, "recall": recall, "f-score": f_score}
