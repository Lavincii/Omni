import speech_recognition as sr #import py library and name it sr
import pyttsx3 #text to speech library
import pywhatkit #package to open youtube videos
import datetime #to get date/time
import wikipedia #installs wiki for quick info
import pyjokes #simple jokes
import requests #request google search, using for weather etc...
#import json

listener = sr.Recognizer() #create variable to recognize your voice
engine = pyttsx3.init() #initialize engine with constructor
voices = engine.getProperty('voices') #collect all provided voices, replace for own, set to variable voices
engine.setProperty('voice', voices[1].id) #set a voice from option menu and set identity of the object
api_key = "4a91b529e813e43207eae1b2eb29551a"
base_url = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={4a91b529e813e43207eae1b2eb29551a}"

def talk(text): #defines a function
    engine.say(text) #speak to user, made dynamic and calls function so machine replies with passed parameter
    engine.runAndWait() #run and wait for response from user


def take_command(): #function for ordering Omni
    try: #to ensure there are no errors thrown
        with sr.Microphone() as source: # source of our audio
            print('listening...') #internal indication,omni is ready
            voice = listener.listen(source) #use microphone as source and call speech recognizer to listen to source
            command = listener.recognize_google(voice) #helps convert voice to text via google API
            #command = command.lower() #converts to lowercase
            if 'Omni' in command: #check if the keyword omni is used
                command = command.replace('Omni', '') #removes the word Omni with empty string so you can make commands
               # print(command) #print command if condition is valid, you could change to talk function and it would repeat back to you
    except:
        pass #runs code
    return command


def run_omni(): #Omni's instructions
    command = take_command() #take command from user ^
    print(command)
    if 'play' in command: #command to play song
        song = command.replace('play', '') #replace the world play with key-phrase
        talk('playing ' + song) # playing ____ example song
        pywhatkit.playonyt(song) #package use to play on youtube
    elif 'time' in command: #if time is mentioned in command
        time = datetime.datetime.now().strftime('%I:%M %p') #get the current time and grab the hr,min, am/pm
        talk('Current time is ' + time) #respond to user
    elif 'who is' in command: #command to query a questions about a person
        person = command.replace('who is', '') #replace "who is" as usual to empty str
        info = wikipedia.summary(person, 1) #call summary method from library and grab a 1 line summary
        print(info) #prints to termianl for me
        talk(info) #Replies to user
    elif 'date' in command: # Ask omni on a date
        talk('sorry, I have a headache') #response
    elif "what's your name" in command:
        talk("I am Omni, a device designed to think and help out humans")
    elif 'are you single' in command: #ask omni if single
        talk('I have no conception of relationships yet') #response
    elif 'joke' in command: #recieve joke
        talk(pyjokes.get_joke()) #give joke from library
    elif 'off' in command: #turn off
        talk("Bye Bye")
        exit()
    elif "that's enough" in command:  # turn off
        exit()
    elif "shut up" in command:
        exit()
    elif "stop" in command:
        exit()
    elif "quit" in command:
        exit()
    elif "thank you" in command:
        talk("No problem")
        exit()
    elif "Dante" in command:
        talk("I cannot talk about my creator, all that I know and well feel is that I love him 100% more than other humans")
    elif "who created you" in command:
        talk("Oh you mean my favorite human in all the world? That would be Dante")
    elif "how are you" in command:
        talk("Well seeing as how I was just born recently... I am doing fantastic")
    elif "that sarcasm" in command:
        talk("No, my voice modulation just is not calibrated properly")
    elif 'weather' in command:
        talk("Which City")
        city_name = take_command()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        talk("Sorry my Internal G P S seems to be malfunctioning")
        # Now x contains list of nested dictionaries
        # Check the value of "cod" key is equal to
        # "404", means city is found otherwise,
        # city is not found
       # if x["cod"] != "404": #change back to x["cod"] != "404"

            # store the value of "main"
            # key in variable y
         #   y = x["Weather_Key"]

            # store the value corresponding
            # to the "temp" key of y
          #  current_temperature = y["temp"]

            # store the value corresponding
            # to the "pressure" key of y
         #   current_pressure = y["pressure"]

            # store the value corresponding
            # to the "humidity" key of y
          #  current_humidiy = y["humidity"]

            # store the value of "weather"
            # key in variable z
         #   z = x["weather"]

            # store the value corresponding
            # to the "description" key at
            # the 0th index of z
         #   weather_description = z[0]["description"]

            # print following values
         #   talk(" Temperature (in kelvin unit) = " +
          ##        str(current_temperature) +
           #       "\n atmospheric pressure (in hPa unit) = " +
            #      str(current_pressure) +
             #     "\n humidity (in percentage) = " +
              #    str(current_humidiy) +
               #   "\n description = " +
                #  str(weather_description))

       # else:
            #talk("Sorry my Internal G P S seems to be malfunctioning")
    else:
        talk("I misunderstood you, what did you say?")


while True: #run Omni until forced to stop
    run_omni()