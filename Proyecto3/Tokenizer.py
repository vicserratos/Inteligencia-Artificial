import string
import en_core_web_sm
nlp = en_core_web_sm.load()

class Tokenizer():
	
	def ejemplo(self, texto):

		print("Tweet: ", texto)

		#Eliminamos puntuacion
		texto = texto.translate(str.maketrans('', '', string.punctuation))
		print("tweet sin puntuacion: ", texto, "\n")

		# Construye el procesador de lenguaje natural
		construccion = nlp (texto)

		# Tokeniza el texto
		lista_tokens = [token for token in construccion]
		print("Lista tokens: ", str(lista_tokens), "\n")

		# Genera una lista de tokens filtrada.
		# El filtro consiste en eliminar palabras conectora o vacias como "pero", "o", "entonces", etc.
		tokens_filtrados = [token for token in construccion if not token.is_stop]
		print("Lista Tokens filtrada: ", tokens_filtrados, "\n")

		#Spicy nos ayuda a normalizar el texto, es decir, las palabras las convierte a su raíz
		# Ejemplo: doctor, doctores, doctoras -> doctor
		# Hay dos formas de normalizar: Derivación y por lemas, Spicy utiliza Lemas
		# Spicy lo hace forma automatica así que se imprime el ejemplo de como funciona
		lemas = [
		    f"Token: {token}, lemma: {token.lemma_}"
		    for token in tokens_filtrados
		]
		print("Ejemplo de lemas: ", lemas, "\n")

		# El siguiente paso es la vectorizacion del texto, lo que se realiza es transformar un token en una matriz
		# Esta matriz en PNL es unica y tiene representadas varias caracteristicas de un token.
		# Esto nos sirve para clasificar el texto dadas sus similitudes.
		print("Vectorizacion de palabras. Ejemplo: ", tokens_filtrados[3], "\n", tokens_filtrados[3].vector, "\n")