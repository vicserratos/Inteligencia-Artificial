
import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

# NOTA!! Descomentar estas dos lineas solo la primera vez!!
nltk.download('punkt')
nltk.download('wordnet')


#Leemos el archivo donde tenemos nuestra base, la cual es un simple txt con un "Tema" y la respuesta que regresara el ChatBot.
with open('data/Comic-OS.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#tokenaizer, creamos tokens con los cuales podemos trabajar
sent_tokens = nltk.sent_tokenize(raw)# convierte las listas en oraciones
word_tokens = nltk.word_tokenize(raw)# Ahora en palabras

#Pre-Procesamiento de la base de datos, aqui preparamos los datos para despues consumirlos
#Convertimos todo a letras minusculas para evitar que Hola y hola, se consideren como palabras diferentes
#Tambien se eliminan cosas incesarias, las cosas que no nos aportan informacion, pueden ser comas, signos, puntos, etc.
# ambos metodos-definiciones, seran utilizadas mas adelante al general la respuesta del chatbot.
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# Los imput son los posibles saludos del usuario, se considera que saludo al ingresar cualquiera de estas palabras
#Los responses son las respuestas del chatbot
GREETING_INPUTS = ("hola", "hi", "holi", "hello")
GREETING_RESPONSES = ["hi", "hey", "hola", "que paso", "como estas", "que pedo", "que onda", "que pex", "que tranza"]

#Si el usuario ingresa un saludo, el chatbot le respondera con uno de los posibles saludos, este se elije de forma aleatoria.
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


#Este es nuestro paso mas importante, pues aqui se genera la respuesta que dara el bot
#Aqui crearemos Vectores, tanto con el contenido de la base como con la entrada de nuestro usuario
#Con esto buscamos una similitud entre lo ingresado por el usuario con los datos en la base, regresando de esta manera
#la respuesta mas parecida segun lo ingresado, en caso de no encontrar coincidencias, se regresa el mensaje donde el chat indica que no conoce de ese tema.
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+" Yo solo se de la Segunda Guerra Mundial, si quieres hablar de algo mas vete con otro chatbot =("
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


#Creamos nuestro main, que contendra el pequeño menu, dando un saludo inicial y las instrucciones de uso del ChatBot
#Como el Chat es quien inicia la interaccion, despues esperamos que el usuario interactue
#una vez obtenermos su interaccion tomamos esta y pasamos a minusculas, si el usuario ingresa "adios", "gracias", "un placer hablar contigo",  "thank you"
#el chatbot se despedira y terminara el programa, en caso contrario si el usuario no ingreso nada, directamente se pasa a el mensaje donde no comprende el tema
#en el ultimo caso se regresara la respues que se calcula en nuestro metodo response.
flag=True
print("Algo: Hola! Te interesa saber sobre la segunda guerra mundial? Preguntame!!!")
print("Algo: Si quieres salir e ignormarme =(...solo escribe adios")  
print("      Tambien puedes ser agradecido y darme las gracias por informarte de tan grandioso tema!!")
print("      Escribe 'algo' y despues dale enter")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='adios'):
        if(user_response=='gracias' or user_response=='thank you' or user_response=='un placer hablar contigo' ):
            flag=False
            print("Algo: De nada!! cuando quieras hablar de la Segunda Guerra Mundial sabes como Ejecutarme =D")
        else:
            if(greeting(user_response)!=None):
                print("Algo: "+greeting(user_response))
            else:
                print("Algo: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("Algo: chao =( no te preocupes, mientras yo me quedare aqui.. hablando solo... solin...solito")
