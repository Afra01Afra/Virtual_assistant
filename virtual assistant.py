import subprocess
import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import json
import feedparser
import smtplib
import datetime 
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)
def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()
    def wish():
        print("Wishing.")
        time = int(datetime.datetime.now().hour)
        global uname,asname
        if time>= 0 and time<12:
            speak("Good Morning sir or madam!")
        elif time<18:
            speak("Good Afternoon sir or madam!")
        else:
            speak("Good Evening sir or madam!")
            asname ="Jasper 1 point o"
            speak("I am your Voice Assistant from DataFlair,")
            speak(asname)
    print("I am your Voice Assistant,",asname)
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)
def takeCommand():
    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)
    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")
    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"
    def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #paste your email id and password in the respective places
    server.login('your email id', 'password') 
    server.sendmail('your email id', to, content)
    server.close()
def getWeather(city_name):
    cityName=place.get() #getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
    response = requests.get(url)
    x = response.json()
    #If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp-=273 
        pressure = y["pressure"]
        humidity = y["humidity"]
        desc = x["weather"]
        description = z[0]["description"]
        info=(" Temperature= " +str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +"\n humidity = " +str(humidity)+"%" +"\n description = " +str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
    else:
        speak(" City Not Found ")
def getNews():
    try:
        response = requests.get('https://www.bbc.com/news')
  
        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']
        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                print(x.text.strip())
    except Exception as e:
        print(str(e))return command




