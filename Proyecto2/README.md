### Proyecto2

## Agente de conversación (chatbot)

Se trata de un ChatBot con el tema de la segunda guerra mundial, al cual se le puede preguntar sobre esta y te dara informacion desde fechas, acontecimientos etc.

[Datos a analizar](./data/Comic-OS.txt)

Se utiliza la biblioteca **NLTK** (Natural Language Toolkit) la cual proporcion muchas herramientas para clasificar texto, tokenizacion, etc. con ayuda de estas herramientas lo primero que debemos hacer es trabajar nuestros datos, pasamos todo el texto a minusculas, para evitar que una misma palabra cuente por dos; despues creamos "Tokens" para pasar de tener cadenas a solo palabras con la ayuda de **nltk.word_tokenize** y **nltk.sent_tokenize**.

El siguiente paso importante es la creacion de una bolsa de palabras, la cual creara vectores, con los cuales despues usando **TF-IDF** nos permite determina la frecuencias con la que un palabra aparece dentro de nuestra base. TF: el numero de veces que un palabra aparece en un parrafo y se divide entre el numero de palabras en ese parrafo. por otro lado IDF: 1+Log(parrafos/numero de parrafos donde aparece una palabra).

Finalmente para que nuestro chatbot nos genere una respuesta utilizaremos un termino llamado **similitud de coceno** la cual hace uso de los vectores que creamos momentos atras, este consiste en un formula donde dados dos vectores (v1,v2) su SC = producto escalar(v1,,v2) / ||v1|| * ||v2||

De esta forma estariamos obteniendo un valor con el cual determinaremos la similitud entro lo que ingresa un usuario como pregunta al chatbot y lo que regresara este como respuesta, por ejemplo el usuario escribe en el chat **Pearl Harbor** esto sera convertido a un vector y se analizara contra la base de datos, esta arrojara resultados intentado empatar los datos de la base con el vecto que le pasamos como pregunta, para despues regresar como respuesta el mejor candidato, si llegaramos a obtener 0 se regresaria un mensaje donde el chatbot indica que no sabe de este tema. 
Para la elaboracion de este ChatBot se tomo como punto de partida un tutorial sobre creacion de ChatBots en python con NLTK, este fue modificado para estar en español, se cambio el tema del chatbot y se creo una base de datos nueva con la cual alimentarlo. Se planeaba usar en su lugar como base el chatbot original de nuestro ayudante de laboratorio, pero quisimos probar este tutorial el cual resulto estar muy bien explicado y asi obtener una fuente extra de conocimiento.

# Ejecutar:
```
$ sudo apt install python
$ pip install nltk
$ python Comic-OS.py (La primera vez que se corre el programa las lineas 17 y 18 deben estar descomentadas, despues se pueden comentar sin problemas)
```

***Tecnologías utilizadas***
* python 3.9.1
* NLTK 3.5
* pip 20.3.3
* numpy 1.19.5
* sklearn 0.0
