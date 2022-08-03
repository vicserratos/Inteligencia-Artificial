from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Tokens de acceso al API de Twitter
access_token = "1352454815612284928-FGSnN5KZBcaYBCn25uqCw5EFtCqq9N"
access_token_secret = "eSpmmgm816u4LL7ri1H2TC03Zcl3pOtziJ2yNlTU7J9Ni"
api_key = "7w0jQUpTHc1IHZ6n7IzlvUomr"
api_secret = "xDURCkqYuUoMDhSWy9txzpx6q3EJByd0HUZ0PXijaDoUMsKjXA"

# Clase que recolecta tweets de acuerdo al tema que vamos a consultar
class ApiTwitter():

    class Streaming(StreamListener):
      
        file = open("tweets.txt", "a")
        
        #def on_data(self, data):
            #print(data)
           # return True

        # Cuando ocurre un error lo cacha e impide que se interrumpa el streaming
        def on_error(self, status):
            print(status)
            
        # Obtiene el tweet y se maneja de acuerdo a lo que queremos, 
        # en nuestro caso nos importa de momento el contenido de tweet.    
        def on_status(self, status):
            #print(status.retweeted_status)
            self.file.write(status.text)
            print(status.text)
            


    def inicalizaStremTwitter(self, palabrasClave): 
        #Inicializa el API
        listener = self.Streaming()
        oAuth = OAuthHandler(api_key, api_secret)
        oAuth.set_access_token(access_token, access_token_secret)
        # inicializa el stream
        streamTwitts = Stream(oAuth, listener)
        
        # asigna filtros al stream
        streamTwitts.filter(track=palabrasClave)