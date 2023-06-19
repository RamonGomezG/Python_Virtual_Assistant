from cgitb import lookup
import pyttsx3
#import pywhatkit
import speech_recognition as sr
import webbrowser
import datetime
import os 
import yfinance as yf 
import pyjokes 
import wikipedia

#funcion que escucha el audio y lo retorna como texto usando google

def transform():
    r = sr.Recognizer()
    with sr.Microphone() as fuente:
        r.pause_threshold = 0.8
        frase = r.listen(fuente)
        try: 
            print ('Recibido')
            q = r.recognize_google(frase, language="es")
            return (q)
        except sr.UnknownValueError:
            print('Perdona no entendi')
            return 'Esperando...'
        except sr.RequestError:
            print('Perdón el servicio esta caido')
            return 'Esperando...'
        except:
            return "Eperando..."

def speaking(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

#Cambiar la voz de la pc 
engine = pyttsx3.init()
id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
engine.setProperty('voice', id)

#retornar el dia de la semana 
def query_day():
    day = datetime.date.today()
    #print(day)
    weekday = day.weekday()
    #print (weekday)
    mapping = {
        0:'Lunes',1:'Martes',2:'Miercoles',3:'Jueves',4:'Viernes',5:'Sabado',6:'Domingo'
    }
    try:
        speaking(f'Hoy es {mapping[weekday]}')
    except:
        pass

#retornar el tiempo
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    print(time)
    speaking(f'Son las {time}')

def welcome():
    speaking('Hola, mi nombre es Sabina y soy tu asistente personal. ¿En qué te puedo ayudar?')

#Funcion principal
def principal():
    welcome()
    start = True 
    while (start):
        q = transform().lower()

        if 'abre youtube' in q:
            speaking('Abriendo Youtube, un segundo.')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'abre google' in q:
            speaking('Abriendo Google, un segundo.')
            webbrowser.open('https://www.google.com')
            continue
        
        elif 'dime la fecha' in q:
            query_day()
            continue
        
        elif 'dime la hora' in q:
            query_time()
            continue

        elif 'apagar' in q:
            speaking('Sale pues')
            break

        elif 'de wikipedia' in q:
            speaking('Buscando en wikipedia')
            q = q.replace('wikipedia' , '')
            result = wikipedia.summary(q, sentences = 2)
            speaking(result)
            continue
        
        elif 'tu nombre' in q:
            speaking('Mi nombre es Sabina')
            continue

        #elif 'en la web' in q:
            pywhatkit.search(q)
            speaking('esto es lo que encontré')
            continue
       

        #elif 'reproduce' in q:
            speaking(f'reproduciendo {q}')
            pywhatkit.playonyt(q)
            continue

        elif 'broma' in q:
            speaking(pyjokes.get_joke())
            continue

        elif 'precio de stock' in q:
            search = q.split('de')[-1].strip()
            lookup = {'apple':'AAPL','amazon':'AMZN','google':'GOOGL'}

            try:
                stock = lookup[search]
                stock = yf.Ticker(stock)
                currentprice = stock.info["regularMarketPrice"]
                speaking(f'lo encontré, el precio de {search} es {currentprice}')
            except:
                speaking('No encontré datos al respecto')
            continue

principal()