#!/usr/bin/python3

import requests
import json
import os
import sys
import datetime
import random
from twilio.rest import Client

account_sid = 'ACCOUNT_SID' #personal sid number here
auth_token = 'AUTH_TOKEN' #personal auth token here
client = Client(account_sid, auth_token)

weatherapi = 'https://api.openweathermap.org/data/2.5/weather?q=Purchase,usa&appid=APP_ID&units=imperial' #personal app id here
jokeapi = 'https://icanhazdadjoke.com/'
kanyeapi = 'https://api.kanye.rest/'
fortuneapi = 'http://fortunecookieapi.herokuapp.com/v1/fortunes?limit=100&skip=&page='
factapi = 'https://uselessfacts.jsph.pl/random.json?language=en'
boredapi = 'http://www.boredapi.com/api/activity/'
adviceapi = 'https://api.adviceslip.com/advice'
quoteapi = 'https://quote-garden.herokuapp.com/quotes/random'

hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
date = str(datetime.datetime.now().date())
json = requests.get(weatherapi).json()
joketext = requests.get(jokeapi, headers={"Accept": "text/plain"})
kanyetext = requests.get(kanyeapi, headers={"Accept": "text/plain"})
fortunetext = requests.get(fortuneapi).json()
facttext = requests.get(factapi).json()
boredtextdata = requests.get(boredapi).json()
advicetextdata = requests.get(adviceapi, headers={"Accept": "text/plain"}).json()
quotetextdata = requests.get(quoteapi).json()

#weather
data = json['weather'][0]['description']
data2 = json['main']['temp']

data2s = str(data2)
fortunedata = fortunetext[random.randint(0,99)]['message']
factdata = facttext['text']
quotetext = quotetextdata['quoteText']
boredtext = boredtextdata['activity']
advicetext = advicetextdata['slip']['advice']

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","y","u","v","w","x","y","z"]
b = ["01100001", "01100010", "01100011", "01100100", "01100101", "01100110", "01100111", "01101000", "01101001", "01101010", "01101011", "01101100", "01101101", "01101110", "01101111", "01110000", "01110001", "01110010", "01110011", "01110100", "01110101", "01110110", "01110111", "01111000", "01111001", "01111010"]

def textMessage(content):
    message = client.messages \
            .create(
                body=content,
                from_='+twilioNumber', #personal Twilio number here
                to='+recipientNumber' #personal number here
            )

def uinput():
    print("(press ctrl + c to quit)")
    l1 = input(">")
    l2 = input(">")
    l3 = input(">")
    l4 = input(">")
    l5 = input(">")
    l6 = input(">")
    l7 = input(">")
    l8 = input(">")
    l9 = input(">")

    return l1, l2, l3, l4, l5, l6, l7, l8, l9

letters = []
letters.append(uinput())

for l1, l2, l3, l4, l5, l6, l7, l8, l9 in letters:
    if (l1, l2) == (b[7], b[8]) or (l1, l2, l3, l4 , l5) == (b[7], b[4], b[11], b[11], b[14]) or (l1, l2, l3) == (b[7], b[4], b[24]):
        print("Hello!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4) == (b[6], b[14], b[14], b[3]):
        print("Cool!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3) == (b[1], b[0], b[3]):
        print(":(")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8 ,l9) == (b[22], b[4], b[0], b[19], b[7], b[4], b[17], "", ""):
        textMessage("If you go outside right now you'll see some " + data + ". The current temperature outside is " + data2s + " degrees.")
        print("Your weather report has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8, l9) == (b[9], b[14], b[10], b[4], "", "", "", "", ""):
        textMessage(joketext.text)
        print("Your joke has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8, l9) == (b[10], b[0], b[13], b[24], b[4], "", "", "", ""):
        textMessage('"' + kanyetext.text + ',"' + ' a wise quote by Kanye West')
        print("You sent a Kanye quote!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8, l9) == (b[5], b[14], b[17], b[19], b[20], b[13], b[4], "", ""):
        textMessage(fortunedata)
        print("You sent a fortune!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8, l9) == (b[15], b[14], b[10], b[4], b[12], b[14], b[13], "", ""):
        try:
            print("Enter a number and I'll tell you which Pokemon is listed under that number in the Pokedex!")
            pinput = int(input(">"))
            if pinput > 1 and pinput < 807:
                pinputs = str(pinput)
                pokeapi = 'http://pokeapi.co/api/v2/pokemon/' + pinputs
                poketext = requests.get(pokeapi).json()
                pdata = poketext['forms'][0]['name']
                textMessage("Number " + pinputs + " in the Pokedex is " + pdata.capitalize() + ".")
                print("Pokemon sent!")
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
            else:
                print("There doesn't seem to be any Pokemon with that number.")
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        except ValueError:
                print("Invalid input. Please type in a number next time!")
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6, l7, l8, l9) == (b[5], b[0], b[2], b[19], "", "", "", "", ""):
        textMessage(factdata)
        print("A fact has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5) == (b[1], b[14], b[17], b[4], b[3]):
        textMessage(boredtext)
        print("An activity has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5, l6) == (b[0], b[3], b[21], b[8], b[2], b[4]):
        textMessage(advicetext)
        print("Advice has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4, l5) == (b[16], b[20], b[14], b[19], b[4]):
        textMessage(quotetext)
        print("An inspirational quote has been sent!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4) == (b[13], b[0], b[12], b[4]):
        print("I don't have a name yet, but I'm working on it.")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3 ,l4) == (b[22], b[7], b[0], b[19]):
        print("I'm a simple chatbot!")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3) == (b[22], b[7], b[24]):
        print("Why do I exist? Why does anything exist at all?")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif (l1, l2, l3, l4) == (b[22], b[7], b[4], b[13]):
        print("I was handed in on December 10, 2019 for a project.")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif(l1, l2, l3, l4) == (b[7], b[4], b[11], b[15]):
        print("a - 01100001")
        print("b - 01100010")
        print("c - 01100011")
        print("d - 01100100")
        print("e - 01100101")
        print("f - 01100110")
        print("g - 01100111")
        print("h - 01101000")
        print("i - 01101001")
        print("j - 01101010")
        print("k - 01101011")
        print("l - 01101100")
        print("m - 01101101")
        print("n - 01101110")
        print("o - 01101111")
        print("p - 01110000")
        print("q - 01110001")
        print("r - 01110010")
        print("s - 01110011")
        print("t - 01110100")
        print("u - 01110101")
        print("v - 01110110")
        print("w - 01110111")
        print("x - 01111000")
        print("y - 01111001")
        print("z - 01111010")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif(l1, l2, l3, l4) == (b[19], b[8], b[12], b[4]):
        print("It is currently " + hour + ":" + minute + ".")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    elif(l1, l2, l3, l4) == (b[3], b[0], b[19], b[4]):
        print("Today's date? " + date + ".")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        print("Sorry, what was that?")
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
