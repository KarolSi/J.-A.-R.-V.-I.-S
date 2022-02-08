from matplotlib.pyplot import text
import speech_recognition as sr
from gtts import gTTS
import time as t
import os
import playsound
import sys
import random as rd
import subprocess as sp
import webbrowser
import pyttsx3 as tts 


#==================================
#-----SPEAK & RECORDING------------
#==================================
'''
engine = tts.init()
engine.setProperty('rate', 125)
engine.setProperty('age', 60)
def mow(text):
    engine.say(text)
    engine.runAndWait()
'''

def speak(text):
    tts = gTTS(text=text, lang = "pl")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound("voice.mp3")  #tu jest problem 
    os.system('cmd /c "del voice.mp3"')
    
    


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nasłuchuję. . .")
        audio = r.listen(source)
        said=""
        try:
                said=r.recognize_google(audio, language="pl")

        except Exception as e:
                print("Czekam na komendę. . ." + str(e))

    return said 





#==================================
#------------AKCJE-----------------
#==================================
def zanotuj():
    #os.chdir('C:\\OneDrive\Porgramowanie\pytong\J. R. V. I. S')
    plik = open('notatka.txt', 'w+')
    speak("co mam zanotować?")
    notatka = get_audio().lower()
    plik.write(notatka)
    print(str(notatka))

def off():
    print("Do widzenia")
    speak("Do widzenia. Miłej reszty dnia")
    quit()
    exit()

def cppspeak():
    print("Nie. Mimo tego, że jest szybszy. Oczywiście wszystko zależy od gustu, ale ja się cieszę, że zostałem napisany w wężu")
    speak("Nie. Mimo tego, że jest szybszy. Oczywiście wszystko zależy od gustu, ale ja się cieszę, że zostałem napisany w wężu")
    
def facebook():
    print("Urachamiam Facebook'a")
    webbrowser.open_new_tab("https://facebook.com")
    speak("okej, poczekaj chwilę")
    

def poczta():
    print("Uruchamiam pocztę")
    webbrowser.open_new_tab("https://n126.domenomania.pl/poczta")
    speak("Już się robi. ciekawe czy masz nowe maile")
 

def instagram():
    print("Otwieram Insta")
    webbrowser.open_new_tab("https://instagram.com")
    speak("Już Się robi szefie")

def wyszkuwinanie():
    print("Co mam wyszukać")
    speak("Co mam wyszukać")
    zmienna = get_audio().lower()
    zmienna = zmienna.replace(' ', '+')
    webbrowser.open_new_tab("https://www.google.com/search?q=" + str(zmienna))
def youtube():
    print("Co mam puścić?")
    speak("co mam puścić?")
    you = get_audio().lower()
    you = you.replace(' ', '++')
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + str(you))
    

def onedrive():
    speak("Otwieranie chmury")
    webbrowser.open_new_tab("https://onedrive.live.com/?id=root&cid=6D766F4CFEF2AED6")
    print("Już włączam")

def solve():
    print("solve")
    webbrowser.open_new_tab("https://solve.edu.pl/contests")
    speak("Otwieranie dzieła Pokora")

def liga():
    print("Już włączam...")
    sp.Popen("C:\Riot Games\League of Legends\LeagueClient.exe")
    speak("Już otwieram. Miłej gry")

def steam():
    print("Się robi...")
    sp.Popen("C:\Program Files (x86)\Steam\Steam.exe")
    speak("Już się robi")

#def discord():
 #   print("Już się robi...")
  #  sp.Popen("C:\Users\karol\AppData\Local\Discord\Update.exe --processStart Discord.exe")
   # speak("Już się otwiera")


#==================================
#-------SPRAWDZANIE KOMEND---------
#==================================
open_text = [" Urachamianie systemów...", "Jarvis melduję się na mostku", "Dzień dobry, 4 bobry"]
los = rd.randint(0, 2)
speak(open_text[los])


def komendy():
    off_commands = ["Wyłącz się", "wyłącz się", "koniec na dziś", "jestem zadowolony z opieki", "Koniec na dziś", "Kończymy", "Jestem zadowolony z opieki" ]
    for phrase in off_commands:
        if phrase in text:
            off()
    
    cpp_opinia = ["czy lubisz C plus plus", "Czy lubisz C plus plus", "co sądzisz o C plus plus"]
    for phrase in cpp_opinia:
        if phrase in text:
            cppspeak()

    notaowanie = ["Zanotuj", "zanotuj", "Zrób notatkę", "zrób notatkę"]
    for phrase in notaowanie:
        if phrase in text:
            zanotuj()
        
    youtu = ["Wyszukaj w YouTubie", "wyszukaj w YouTubie", "Wyszukaj w YouTubie", "Puść muzykę"]
    for phrase in youtu:
        if phrase in text:
            youtube()

    google = ["wygoogluj", "Wygoogluj", "Wyszukaj w internecie", "wyszukaj w internecie"]
    for phrase in google:
        if phrase in text:
            wyszkuwinanie()
        
    mail = ["Otwórz proszę pocztę","Maila otwórz", "maila otwórz","włącz pocztę", "Włącz pocztę","Włącz pocztę", "włącz poczte", "otwórz proszę poczte", "Otwórz maila","otwórz maila", "Odpal skrzynkę", "odpal skrzynkę", "odpal pocztę", "Odpal pocztę"]
    for phrase in mail:
        if phrase in text:
            poczta()
    
    fejs = ["Otwórz proszę fejsa"," otwórz proszę fejsa", "Odpal Facebooka", "odpal Fejsa", "Włącz Facebooka", "włącz Facebooka"]
    for phrase in fejs:
        if phrase in text:
            facebook()

    ig = ["Odpal Insta","odpal Insta", "otwórz instagrama", "Otwórz Instagrama"]
    for phrase in ig:
        if phrase in text:
            instagram()

    lol = ["Ligusia", "ligusia", "Liga", "liga","ligę","Ligę", "Lola", "lola" ]
    for phrase in lol:
        if phrase in text:
            liga()
        
    #dic = ["Discord", "discord", "Discorda", "discorda"]
    #for phrase in dic:
     #   if phrase in text:
      #      discord()   
        
    oned = ["Chmurę", "chmurę", "Onedriva", "onedriva"]
    for phrase in oned:
        if phrase in text:
            onedrive()
    
    solv = ["Solva", "solva"]
    for phrase in solv:
        if phrase in text:
            solve()







#-------------GŁÓWNA PĘTLA-------------------

speak(" Gotowość w 100%")

while (1):
    
    text = get_audio()
    print(text)
    komendy()

