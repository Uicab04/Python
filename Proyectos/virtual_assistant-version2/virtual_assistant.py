'''
    Description:
    Create your own virtual assistant with Python.

    Author: AlejandroV
    Version: 2.0
    Video: https://youtu.be/Cr9O31eqXuA
'''
from cmd import PROMPT
import AVMSpeechMath as sm
import AVMYT as yt
import spoty
import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
from datetime import datetime, date, timedelta
import wikipedia
import pyjokes
from time import time
import os
import openai

openai.api_key = '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'

start_time = time()
engine = pyttsx3.init()

# name of the virtual assistant
name = 'alexa'
attemts = 0

# keys
with open('src/keys.json') as json_file:
    keys = json.load(json_file)

# colors
green_color = "\033[1;32;40m"
red_color = "\033[1;31;40m"
normal_color = "\033[0;37;40m"

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.7)

day_es = [line.rstrip('\n') for line in open('src/day/day_es.txt')]
day_en = [line.rstrip('\n') for line in open('src/day/day_en.txt')]

def iterateDays(now):
    for i in range(len(day_en)):
        if day_en[i] in now:
            now = now.replace(day_en[i], day_es[i])
    return now

def getDay():
    now = date.today().strftime("%A, %d de %B del %Y").lower()
    return iterateDays(now)

def getDaysAgo(rec):
    value =""
    if 'ayer' in rec:
        days = 1
        value = 'ayer'
    elif 'antier' in rec:
        days = 2
        value = 'antier'
    else:
        rec = rec.replace(",","")
        rec = rec.split()
        days = 0

        for i in range(len(rec)):
            try:
                days = float(rec[i])
                break
            except:
                pass
    
    if days != 0:
        try:
            now = date.today() - timedelta(days=days)
            now = now.strftime("%A, %d de %B del %Y").lower()

            if value != "":
                return f"{value} fue {iterateDays(now)}"
            else:
                return f"Hace {days} días fue {iterateDays(now)}"
        except:
            return "Aún no existíamos"
    else:
        return "No entendí"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    status = False

    with sr.Microphone() as source:
        print(f"{green_color}({attemts}) Escuchando...{normal_color}")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        rec = ""

        try:
            rec = r.recognize_google(audio, language='es-ES').lower()
            
            if name in rec:
                rec = rec.replace(f"{name} ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
                status = True
            else:
                print(f"Vuelve a intentarlo, no reconozco: {rec}")
        except:
            pass
    return {'text':rec, 'status':status}

while True:
    rec_json = get_audio()

    rec = rec_json['text']
    status = rec_json['status']

    print(rec_json)

    if status:
        if 'estas ahi' in rec:
            speak('Por supuesto')

        elif 'reproduce' in rec:
            if 'spotify' in rec:
                music = rec.replace('reproduce en spotify', '')
                speak(f'Reproduciendo {music}')
                spoty.play(keys["spoty_client_id"], keys["spoty_client_secret"], music)
            else:
                music = rec.replace('reproduce', '')
                speak(f'Reproduciendo {music}')
                pywhatkit.playonyt(music)
                # yt.play(music)

        elif 'cuantos suscriptores tiene' in rec:
            name_subs = rec.replace('cuantos suscriptores tiene', '')
            
            speak("Procesando...")
            while True:
                try:
                    channel = yt.getChannelInfo(name_subs)
                    speak(channel["name"] + " tiene " + channel["subs"])
                    break
                except:
                    speak("Volviendo a intentar...")
                    continue

        elif 'que' in rec:
            if 'hora' in rec:
                hora = datetime.now().strftime('%I:%M %p')
                speak(f"Son las {hora}")

            elif 'dia' in rec:
                if 'fue' in rec:
                    speak(f"{getDaysAgo(rec)}")
                else:
                    speak(f"Hoy es {getDay()}")

        elif 'busca' in rec:
            order = rec.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            speak(info)

        elif 'chiste' in rec:
            chiste = pyjokes.get_joke("es")
            speak(chiste)

        elif 'cuanto es' in rec:
            speak(sm.getResult(rec))

        elif 'descansa' in rec:
            speak("Saliendo...")
            break

        else:
            start_sequence = "\nA:"
            restart_sequence = "\n\nQ: "
            question = str(rec)
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt="Soy un bot de respuesta a preguntas muy inteligente.\n\nQ: " + question + " \nA:",
                temperature=0.7,
                max_tokens=3000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n"]
            )


            anwer = response.choices[0].text.strip()
            
            print("AI: " + anwer + "\n")
            speak(anwer)
        attemts += 1
    else:
        # start_sequence = "\nA:"
        # restart_sequence = "\n\nQ: "
        # question = str(rec)
        # response = openai.Completion.create(
        #     model="text-davinci-002",
        #     prompt="Soy un bot de respuesta a preguntas muy inteligente. Si me haces una pregunta que tiene sus raíces en la verdad, te daré la respuesta. Si me hace una pregunta que es una tontería, un engaño o que no tiene una respuesta clara, le responderé con \"Desconocido\".\n\nQ: " + question + " \nA:",
        #     temperature=0,
        #     max_tokens=500,
        #     top_p=1,
        #     frequency_penalty=0,
        #     presence_penalty=0,
        #     stop=["\n"]
        # )


        # anwer = response.choices[0].text.strip()
            
        # print("AI: " + anwer + "\n")
        # speak(anwer)


        attemts += 1

print(f"{red_color} PROGRAMA FINALIZADO CON UNA DURACIÓN DE: { int(time() - start_time) } SEGUNDOS {normal_color}")