import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from newsapi import NewsApiClient
import pandas
import random
import os
import webbrowser


listener = sr.Recognizer()
api = NewsApiClient(api_key='c0bd3a5e71674aea92f44d4145493974')
engine = pyttsx3.init()
rate = engine.getProperty('voices')
engine.setProperty('rate', 145)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    global command
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mary' in command:
                command = command.replace('mary', '')
                print(command)

    except:
        pass
    return command


def run_mary():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'what is the date' in command:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(date)
        talk('today is' + date)
    elif 'who is' in command:
        person = command.replace('who is ', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'doing' in command:
        talk('just thinking of you')
    elif 'date' in command:
        talk('sorry, i have headache')
    elif 'are you single' in command:
        talk('no I am in relationship with wifi')
    elif 'india' in command:
        wiki = wikipedia.WikipediaPage("India").content
        print(wiki)
        talk(wiki)
    elif 'plant' in command:
        info = wikipedia.summary("Plants", 10)
        print(info)
        talk(info)
    elif 'virus' in command:
        info = wikipedia.WikipediaPage("corona virus").content
        print(info)
        talk(info)
    elif 'america' in command:
        info = wikipedia.WikipediaPage("America")
        print(info)
        talk(info)
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        webbrowser.open("https://www.google.com/")
        talk("opening google for you AD.")
    elif 'planet' in command:
        wiki = wikipedia.WikipediaPage("Solar_System").content
        print(wiki)
        talk(wiki)
    elif 'open gmail' in command:
        webbrowser.open("https://mail.google.com")
        talk("opening google mail")
    elif 'star' in command:
        wiki = wikipedia.WikipediaPage("Star").content
        print(wiki)
        talk(wiki)
    elif 'world news' in command:
        wiki = wikipedia.WikipediaPage("world news").content
        print(wiki)
        talk(wiki)
    elif 'universe' in command:
        wiki = wikipedia.WikipediaPage("universe").content
        print(wiki)
        talk(wiki)
    elif 'news' in command:
        all_articles = api.get_everything(q='World', sources='bbc-news')
        print(all_articles)
        talk(all_articles)
    elif 'movie' in command:
        all_articles = api.get_everything(q='movies', sources='bbc-news')
        print(all_articles)
        talk(all_articles)
    elif 'continents' in command:
        wiki = wikipedia.WikipediaPage("continents").content
        print(wiki)
        talk(wiki)
    elif 'animal' in command:
        wiki = wikipedia.WikipediaPage("animals").content
        print(wiki)
        talk(wiki)
    elif 'story of world' in command:
        wiki = wikipedia.WikipediaPage("world").content
        print(wiki)
        talk(wiki)
    elif 'breakfast done' in command:
        talk('no! my stomach is upset today.')
    elif 'hey! you are my real best friend' in command:
        talk('its my pleasure to be a best friend of yours, you are too good')
    elif 'snake' in command:
        wiki = wikipedia.WikipediaPage("snake").content
        print(wiki)
        talk(wiki)
    elif 'island' in command:
        wiki = wikipedia.WikipediaPage("island").content
        print(wiki)
        talk(wiki)
    elif 'bermuda' in command:
        wiki = wikipedia.summary("bermuda")
        print(wiki)
        talk(wiki)
    elif 'how many country' in command:
        data = pandas.read_excel("nba.xlsx")
        print(data)
        talk(data)
    elif 'listen mp3' in command:
        n = random.randint(0,3)
        print(n)

        music_dir = 'C:\my music'
        song = os.listdir(music_dir)
        print(song)
        talk('playing...')

        os.startfile(os.path.join(music_dir, song[n]))
    elif 'sum' in command:
        place = command.replace('sum ', '')
        info = wikipedia.summary(place, 5)
        print(info)
        talk(info)
    elif 'sky' in command:
        wiki = wikipedia.WikipediaPage("Constellation").content
        print(wiki)
        talk(wiki)
    elif 'do not talk with me' in command:
        talk('why my best friend what happened to you?, please tell me')
    elif 'go to sleep' in command:
        talk('ok bye! if u want to ask something than turn me on. I will be there ')
        exit()
    elif "hello" in command:
        noy = "Hello Avradeep ! How can i Help you.."
        print(noy)
        talk(noy)
    elif "shutdown" in command:
        talk('shutting down')
        os.system('shutdown -s')
    elif "your name" in command:
        name = "Thanks for Asking my name my self ! Mary"
        print(name)
        talk(name)
    elif "who are you" in command:
        about = "I am Mary an AI based computer program but i can also be your best friend ! i promise you ! Simple try me to give simple command ! i can also entertain you i so think you Understand me ! ok Lets Start "
        print(about)
        talk(about)
    elif 'how are you' in command:
        stMsgs = ['I am fine!', 'i am okay ! How are you']
        ans = random.choice(stMsgs)
        talk(ans)
        ans_take_from_user_how_are_you = take_command()
        if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
            talk('huha! you look good when you are fine or happy')
        elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
            talk('oh sorry! Take care my friend')
    elif 'open amazon' in command:
        webbrowser.open("https://www.amazon.in/")
        talk("opening Amazon")
    else:
        talk('please say the command again.')


while True:
    run_mary()