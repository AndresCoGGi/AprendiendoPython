import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar el recognizer en una variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # imformar que empezo la grabacion
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google lo escuhado
            pedido = r.recognize_google(audio, language='es-CO')

            # prueba de que pudo ingresar
            print("Dijiste: "+pedido)

            # devolver a pedido
            return pedido
        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups, no entendi")

            # devolver error
            return "sigo esperando el audio"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # devolver error
            return "sigo esperando el audio"

        # error inesperado
        except:
            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "sigo esperando el audio"

# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # engine = pyttsx3.init()
    # averiguar voces del sistema
    # for voz in engine.getProperty('voices'):
    #   print(voz)
    id_voz_sabina = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id_voz_sabina)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

# informar el dia de la semana
def pedir_dia():

    #crear variables con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario que contenga el nombre de los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    hablar(f'Hoy es {calendario[dia_semana]}')

#pedir hora
def pedir_hora():

    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)

# saludo
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 19:
        momento = 'Buenas Noches'
    elif 6 <= hora.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    #decir el saludo
    hablar(f'{momento} Andru, soy Sabina, tu asistente personal. Por favor, dime en que te puedo ayudar')

# Funcion central del asistente
def  pedir_cosas():

    #activar el saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:

        # activar el micro y guardar le pedido en un String
        pedido = transformar_audio_en_texto().lower()

        if 'abrir google' in pedido:
            hablar('Con gusto, estoy abriendo Google')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://m365.cloud.microsoft/apps/?auth=2&origindomain=Office')
            continue
        elif 'que dia es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar(f'Wikipendia dice esto: {resultado}')
        elif 'busca en internet' in pedido:
            hablar('Ok, consultando')
            pywhatkit.search(pedido.replace('busca en internet',''))
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea, ya lo reproduzco')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))



pedir_cosas()