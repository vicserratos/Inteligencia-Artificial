### Proyecto 3 

## Analizador de Sentimientos de Redes Sociales

Es un analizador de sentimientos en redes sociales

***Code:***

[Formato Jupyter para vizualizar el proceso](ApiTwitter.ipynb)

[Formato .py para ejecutar](AnalizadorSentimientos.py)

# **Instalación de dependencias y configuración:**
```
# Python y pip
$ sudo apt install python3
$ sudo apt install python3-pip

# Genera un ambiente para el uso de las dependencias
$ sudo apt install python3-venv
$ python3 -m venv .analizador
$ source .analizador/bin/activate

# Dependencias
$ pip3 install tweepy
$ pip3 install spacy==2.3.2
$ python3 -m spacy download en_core_web_sm
```

# **Ejecución:**
```
$ python3 AnalizadorSentimientos.py
```

# **Salir y limpiar ambiente:**
```
$ deactivate
$ rm -r .analizador
$ rm -r __pycache__
$ rm -r modeloData (si quieres eliminar el modelo generado)
```

***Tecnologías utilizadas***
* Python 3
* Tweepy
* spaCy
* IPython Notebook
* Twitter
