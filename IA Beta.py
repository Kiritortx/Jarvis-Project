# Importa a biblioteca
import speech_recognition as sr
import pyttsx3 as tts 
import webbrowser as wb
import os

# Inicializa o tts
tts.init()

# Inicializa o reconhecedor
engine = tts.init()
texto = "Oi, eu sou a Let, a sua assistente pessoal. Como posso ajudar?"

# Fala o texto
engine.say(texto)
engine.runAndWait()

# Cria um reconhecedor
rec = sr.Recognizer()

# Faz o reconhecimento usando supressão de ruido
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

# Printa o que voce disse
print("Voce disse: " + texto)

# Funções
if "google" in texto.lower():
    opera_path = r"C:\Users\pedro\AppData\Local\Programs\Opera GX\opera.exe"
    wb.register('opera', None, wb.BackgroundBrowser(opera_path))
    wb.get('opera').open_new_tab('https://www.google.com')
if "chat" in texto.lower():
    opera_path = r"C:\Users\pedro\AppData\Local\Programs\Opera GX\opera.exe"
    wb.register('opera', None, wb.BackgroundBrowser(opera_path))
    wb.get('opera').open_new_tab('https://chatgpt.com')
if "youtube" in texto.lower():
    opera_path = r"C:\Users\pedro\AppData\Local\Programs\Opera GX\opera.exe"
    wb.register('opera', None, wb.BackgroundBrowser(opera_path))
    wb.get('opera').open_new_tab('https://www.youtube.com')
if "spotify" in texto.lower():
    opera_path = r"C:\Users\pedro\AppData\Local\Programs\Opera GX\opera.exe"
    wb.register('opera', None, wb.BackgroundBrowser(opera_path))
    wb.get('opera').open_new_tab('https://open.spotify.com')
