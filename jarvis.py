from unittest import skip
from matplotlib.pyplot import text
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import sys
import random as rd
import subprocess as sp
import webbrowser
import pyttsx3 as tts 
import socket
from tkinter import *
from tkinter import ttk
import turtle 
import datetime




#==================================
#-------SPEAK & RECORDING----------
#==================================

'''
engine = tts.init()
engine.setProperty('rate', 125)
engine.setProperty('age', 60)
def mow(t):
    engine.say(t)
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


#--------PRZWITANIE SIĘ-----------

open_text = [" Uruchamianie systemów...", "Jarvis melduję się na mostku", "Dzień dobry, 4 bobry"]
los = rd.randint(0, 2)
speak(open_text[los])

#==================================
#-------USTAIWNIA OKIENKA----------
#==================================


#==================================
#------Podłączenie do Serwera------
#==================================
speak("Czy mam się łączyć z serwerem?")
t = get_audio()
if("Tak"==t):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    speak("łączenie z serwerami")  
    s.connect(('localhost', 8008)) 
    print(s.getsockname())
else:
    skip


    

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
    global t
    t = t.replace("Wyszukaj ", "")
    t = t.replace(' ', '+')
    webbrowser.open_new_tab("https://www.google.com/search?q=" + str(t))

def youtube():
    global t
    #print("Co mam puścić?")
    #speak("co mam puścić?")
    #you = get_audio().lower()
    
    t = t.replace("Puść ", "")
    t = t.replace(' ', '++')
    webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + str(t))
    

def onedrive():
    speak("Otwieranie chmury")
    webbrowser.open_new_tab("https://onedrive.live.com/?id=root&cid=6D766F4CFEF2AED6")
    print("Już włączam")

def solve():
    print("otwieranie solve'a")
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

def serwer():
    print("próba łączności")
    speak("próba łączności")
    s.sendall(b'example')
    data = s.recv(1024)
    print(data)
    if(b'we have connectionco\xc5\x9bpc: OK'==data):
        speak("mamy to, połączenie zostało nawiązane")

def czas():
    print(str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute))
    speak("jest " + str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute))


#def discord():
 #   print("Już się robi...")
  #  sp.Popen("C:\Users\karol\AppData\Local\Discord\Update.exe --processStart Discord.exe")
   # speak("Już się otwiera")

def czuwam():
    print("Dla Pana zawsze")
    speak("dla Pana zawsze")

#==================================
#-------SPRAWDZANIE KOMEND---------
#==================================



def komendy():
    off_commands = ["Wyłącz się", "wyłącz się", "koniec na dziś", "jestem zadowolony z opieki", "Koniec na dziś", "Kończymy", "Jestem zadowolony z opieki" ]
    for phrase in off_commands:
        if phrase in t:
            off()
    
    cpp_opinia = ["czy lubisz C plus plus", "Czy lubisz C plus plus", "co sądzisz o C plus plus"]
    for phrase in cpp_opinia:
        if phrase in t:
            cppspeak()

    notaowanie = ["Zanotuj", "zanotuj", "Zrób notatkę", "zrób notatkę"]
    for phrase in notaowanie:
        if phrase in t:
            zanotuj()
        
    youtu = ["Wyszukaj w YouTubie", "wyszukaj w YouTubie", "Wyszukaj w YouTubie", "Puść muzykę", "Puść", "puść"]
    for phrase in youtu:
        if phrase in t:
            youtube()

    google = ["wygoogluj", "Wygoogluj", "Wyszukaj w internecie", "wyszukaj w internecie", "wyszukaj", "Wyszukaj"]
    for phrase in google:
        if phrase in t:
            wyszkuwinanie()
        
    mail = ["Otwórz proszę pocztę","Maila otwórz", "maila otwórz","włącz pocztę", "Włącz pocztę","Włącz pocztę", "włącz poczte", "otwórz proszę poczte", "Otwórz maila","otwórz maila", "Odpal skrzynkę", "odpal skrzynkę", "odpal pocztę", "Odpal pocztę"]
    for phrase in mail:
        if phrase in t:
            poczta()
    
    fejs = ["Otwórz proszę fejsa"," otwórz proszę fejsa", "Odpal Facebooka", "odpal Fejsa", "Włącz Facebooka", "włącz Facebooka"]
    for phrase in fejs:
        if phrase in t:
            facebook()

    ig = ["Odpal Insta","odpal Insta", "otwórz instagrama", "Otwórz Instagrama"]
    for phrase in ig:
        if phrase in t:
            instagram()

    lol = ["Ligusia", "ligusia", "Liga", "liga","ligę","Ligę", "Lola", "lola" ]
    for phrase in lol:
        if phrase in t:
            liga()
        
    #dic = ["Discord", "discord", "Discorda", "discorda"]
    #for phrase in dic:
     #   if phrase in t:
      #      discord()   
        
    oned = ["Chmurę", "chmurę", "Onedriva", "onedriva"]
    for phrase in oned:
        if phrase in t:
            onedrive()
    
    solv = ["Solva", "solva"]
    for phrase in solv:
        if phrase in t:
            solve()
    
    serw = ["Próba", "próba"]
    for phrase in serw:
        if phrase in t:
            serwer()

    jestes = ["czuwasz", "Jarvis jesteś tam"]
    for phrase in jestes:
        if phrase in t:
            czuwam()

    hour = ["Która jest godzina", "Jaki czas mamy"]
    for phrase in hour:
        if phrase in t:
            czas():











#-------------GŁÓWNA PĘTLA-------------------

speak(" Gotowość w 100%")

while (1):
    
    t = get_audio()
    print(t)
    komendy()

