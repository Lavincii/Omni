import tkinter as tk
#from tkinter import filedialog, Text
import os
import speech_recognition as sr  # import py library and name it sr
import pyttsx3  # text to speech library
import pywhatkit  # package to open youtube videos
import datetime  # to get date/time
import wikipedia  # installs wiki for quick info
import pyjokes  # simple jokes
from tkinter import *
import requests  # request google search, using for weather etc...
import csv

# import json

root = tk.Tk()
def Activate():

    listener = sr.Recognizer()  # create variable to recognize your voice
    engine = pyttsx3.init()  # initialize engine with constructor
    voices = engine.getProperty('voices')  # collect all provided voices, replace for own, set to variable voices
    engine.setProperty('voice', voices[0].id)  # set a voice from option menu and set identity of the object


    def talk(text):  # defines a function
        engine.say(text)  # speak to user, made dynamic and calls function so machine replies with passed parameter
        engine.runAndWait()  # run and wait for response from user

    def take_command():  # function for ordering Omni
        try:  # to ensure there are no errors thrown
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
               # talk('listening') #erase later
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                command = listener.recognize_google(voice)  # helps convert voice to text via google API
                command = command.lower()
                if 'Omni' in command:  # check if the wakeword omni is used
                    command = command.replace('Omni', '')
                    # command = command.lower() #converts to lowercase
                else:
                    pass
                    #print(command) #print command if condition is valid, you could change to talk function and it would repeat back to you
        except:
            pass  # runs code
        return command

    def run_omni():  # Omni's instructions
        import time  # retrieve current time
        from playsound import playsound  # used for playing alarm
        from datetime import datetime
        import speech_recognition as sr

        command = take_command()  # take command from user ^
        print(command)

        if 'learn something' in command:
            talk("What would you like me to learn?")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                learning_command = listener.recognize_google(voice)
                print(learning_command)
                if "i would like you to learn" in learning_command:
                    learning_command.replace("I would like you to learn", '')
                elif "learn" in learning_command:
                    learning_command.replace("learn", '')
                elif "please learn" in learning_command:
                    learning_command.replace("please learn", '')
                else:
                    pass
            # store learning command in memory
            #skill_memory = []
           # skill_memory = learning_command
           # print(skill_memory)#uncomment to test success

            #teaching process
            talk("In order to teach me " + learning_command + " I need some help, so allow me to ask a few questions")
            talk("What is the first step")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                procedure_command = listener.recognize_google(voice)
                print(procedure_command)
            if "first step" in procedure_command:
                print("wait")
            elif "next step" in procedure_command:
                print("wait")

            take_command()

        elif 'learn exact' in command:
            talk("What is it you'd like to define")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                def_command = listener.recognize_google(voice)
                print(def_command)
            definition_title = def_command

            talk("Now what does that mean?")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                defans_command = listener.recognize_google(voice)
                print(defans_command)
                def_answer = defans_command

            def manualentry():

                # Open csv file at start
                outfile = open('definitions.csv', 'a', newline='')
                w = csv.writer(outfile)  # Need to write the user input to the .csv file.
                # Everything wrapped in a while True loop, you can change to any loop accordingly
                while True:
                    title = definition_title  # Generate data for each column to fill in to the output file.
                    definition = def_answer  # Each line asks the user to add data do the line.
                    print(title, definition)  # Prints the line of user data
                    talk("Does everything look okay")
                    with sr.Microphone() as source:  # source of our audio
                        print('listening...')  # internal indication,omni is ready
                        voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                        update_command = listener.recognize_google(voice)
                        print(update_command)
                    if "yes" in update_command:
                        w.writerow([title, definition])  # <-This is the portion that seems to fall apart.
                        print("INVENTORY UPDATED")
                        return take_command()
                    elif "no" in update_command:
                        print("SKIPPING. RESTARTING....")
                    # If you see stop, stop writing, close the file and exit
                    elif "stop" in update_command:
                        talk("hmmm, so that's all?")
                        outfile.close()
                        return take_command()
                    else:
                        talk("I couldn't quite understand you so I'm going to leave that last part out.")
                        return take_command()
            # Call manualentry
            manualentry()
        elif 'give me a definition' in command:
            data = []
            with open("definitions.csv") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    data.append(row)
                    #print data
            talk("What would you like the definition of?")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                search_prompt = listener.recognize_google(voice)
                print(search_prompt)
                search_prompt = search_prompt.replace("what is the definition of", '')
                search_prompt = search_prompt.replace("what is", '')
                search_prompt = search_prompt.replace("what is a", '')
                search_prompt = search_prompt.replace("what is the", '')

            search = search_prompt
            col = [x[0] for x in data]
            if search in col:
                for x in range(0, len(data)):
                    if search == data[x][0]:
                        print(data[x])
                        newstring =str(data[x])
                        talk(newstring)
                    else:
                        pass

        elif'look something up' in command:
            import requests
            talk("what would you like me to look up")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                search_prompt = listener.recognize_google(voice)
                print(search_prompt)
            query = search_prompt

            r = requests.get("https://api.duckduckgo.com",
                             params={
                                 "q": query,
                                 "format": "json"
                             })

            data = r.json()
            if True:
                newline = str(data["Abstract"])
                talk(newline)
            else:
                talk("I couldn't find that on the web, sorry.")
        elif 'play' in command:  # command to play song
            song = command.replace('play', '')  # replace the world play with key-phrase
            talk('playing ' + song)  # playing ____ example song
            pywhatkit.playonyt(song)  # package use to play on youtube
            take_command()
        elif 'time' in command:  # if time is mentioned in command
            time = datetime.now().strftime('%I:%M %p')  # get the current time and grab the hr,min, am/pm
            talk('Current time is ' + time)  # respond to user
            take_command()
        elif 'who is' in command:  # command to query a questions about a person
            person = command.replace('who is', '')  # replace "who is" as usual to empty str
            info = wikipedia.summary(person, 1)  # call summary method from library and grab a 1 line summary
            print(info)  # prints to terminal for me
            talk(info)  # Replies to user
        elif 'do you know' in command:  # command to query a questions about a person
            person = command.replace('do you know', '')
            info = wikipedia.summary(person, 1)  # call summary method from library and grab a 1 line summary
            print(info)  # prints to terminal for me
            talk(info)  # Replies to user
        elif "predict the closing price of" in command:
            import numpy as np
            import matplotlib.pyplot as plt
            import pandas as pd
            import pandas_datareader as web
            import datetime as dt

            from sklearn.preprocessing import MinMaxScaler
            from tensorflow.keras.models import Sequential
            from tensorflow.keras.layers import Dense, Dropout, LSTM

            #talk("Which company would you like to predict the next day closing price for?")
            if "tesla" in command:
                company = 'TSLA'#hardcoded ticker
                print("predicting tesla")
            elif "apple" in command:
                company = 'AAPL'
                print("predicting apple")
            elif "facebook" in command:
                company = 'FB'
                print("predicting facebook")
            elif "amazon" in command:
                company = 'AMZN'
                print("predicting amazon")
            else:
                talk("What is the ticker symbol")
                with sr.Microphone() as source:  # source of our audio
                    print('listening...')  # internal indication,omni is ready
                    voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                    company_command = listener.recognize_google(voice)
                    print(company_command)
                company = company_command

            start = dt.datetime(2012,1,1)
            end = dt.datetime(2021,1,1)
            data = web.DataReader(company, 'yahoo', start, end)
            if company not in data:
                print("company not found")

            #prepare Data
            scaler = MinMaxScaler(feature_range=(0,1))
            scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))
            prediction_days = 60 #how far back you wish to predict
            x_train = []
            y_train = []
            for x in range(prediction_days, len(scaled_data)):
                x_train.append(scaled_data[x-prediction_days:x, 0])
                y_train.append(scaled_data[x, 0])
            x_train, y_train = np.array(x_train), np.array(y_train)
            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
            # Build the model
            model = Sequential()
            model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50, return_sequences=True))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50))
            model.add(Dropout(0.2))
            model.add(Dense(units=1)) #prediction of the next closing price
            model.compile(optimizer='adam', loss='mean_squared_error')
            model.fit(x_train, y_train, epochs=25, batch_size=32)
            '''Test The Model Accuracy on Existing Data '''
            #Load Test Data
            test_start = dt.datetime(2021,1,1)
            test_end = dt.datetime.now()
            test_data = web.DataReader(company, 'yahoo', test_start, test_end)
            #Get prices and concatenate dataset
            actual_prices = test_data['Close'].values
            total_dataset = pd.concat((data['Close'], test_data['Close']), axis=0)
            model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
            model_inputs = model_inputs.reshape(-1, 1)
            model_inputs = scaler.transform(model_inputs)
            #Make Predictions on test Data
            x_test = []
            for x in range(prediction_days, len(model_inputs)):
                x_test.append(model_inputs[x-prediction_days:x, 0])
            x_test = np.array(x_test)
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
            predicted_prices = model.predict(x_test)
            predicted_prices = scaler.inverse_transform(predicted_prices)
            #Plot the test Predictions
            plt.plot(actual_prices, color = "black", label =f"Actual {company} Price")
            plt.plot(predicted_prices, color = 'green', label=f"Predicted {company} Price")
            plt.title(f"{company} Share Price")
            plt.xlabel('Time')
            plt.ylabel(f'{company} Share Price')
            plt.legend()
            plt.show()
            #Predicting Future Days
            real_data = [model[len(model_inputs) + 1 - prediction_days:len(model_inputs+1), 0]]
            real_data = np.array(real_data)
            real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1],1))
            prediction = model.predict(real_data)
            prediction = scaler.inverse_transform(prediction)
            print(f"Prediction: {prediction}")
            take_command()
            #talk(f"The stock price of {company}")

        elif "set an alarm" in command:
            talk("an alarm for what time")
            #string = command.replace("set an alarm", "")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(source)  # use microphone as source and call speech recognizer to listen to source
                new_command = listener.recognize_google(voice)
                print(new_command)
                if " p.m." in new_command:
                    alarmtime = new_command.replace(" p.m.", "")
                elif " a.m." in new_command:
                    alarmtime = new_command.replace(" a.m.", "")
                else:
                    pass
                print(alarmtime)
            #alarmtime = "16:24" #hardcorded alarm
            #alarmtime = input("Set Time: ") #input from console
            talk("Alarm set for" + alarmtime) #respond to user
            while True:
                local_time = datetime.now().strftime('%I:%M').lstrip("0").replace(" 0", " ")#set local time and remove zero padding
                if local_time == "1:00" or "2:00" or "3:00" or "4:00" or "5:00" or "6:00" or "7:00" or "8:00" or "9:00" or "10:00" or "11:00" or "12:00":
                    local_time = local_time.replace(":00", "")
                else:
                    pass
                if local_time == alarmtime: #play sound if alarm equals local time
                    playsound('alarm.wav') #alarm sound
                    break
                else:
                    print(local_time) #to show console is waiting
                    time.sleep(10) #set wait time for machine to recheck time
            take_command()
        elif "set an alarm for" in command:
            talk("an alarm for what time")
            # string = command.replace("set an alarm", "")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')  # internal indication,omni is ready
                voice = listener.listen(
                    source)  # use microphone as source and call speech recognizer to listen to source
                new_command = listener.recognize_google(voice)
                print(new_command)
                if " p.m." in new_command:
                    alarmtime = new_command.replace(" p.m.", "")
                elif " a.m." in new_command:
                    alarmtime = new_command.replace(" a.m.", "")
                else:
                    pass
                print(alarmtime)
            # alarmtime = "16:24" #hardcorded alarm
            # alarmtime = input("Set Time: ") #input from console
            talk("Alarm set for" + alarmtime)  # respond to user
            while True:
                local_time = datetime.now().strftime('%I:%M').lstrip("0").replace(" 0",
                                                                                  " ")  # set local time and remove zero padding
                if local_time == "1:00" or "2:00" or "3:00" or "4:00" or "5:00" or "6:00" or "7:00" or "8:00" or "9:00" or "10:00" or "11:00" or "12:00":
                    local_time = local_time.replace(":00", "")
                else:
                    pass

                if local_time == alarmtime:  # play sound if alarm equals local time
                    playsound('alarm.wav')  # alarm sound
                    break
                else:
                    print(local_time)  # to show console is waiting
                    time.sleep(10)  # set wait time for machine to recheck time
            take_command()
        elif "set a reminder" in command:
            import time
            talk("What shall I remind you about?")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')
                voice = listener.listen(source)
                reminder_command = listener.recognize_google(voice)
                print(reminder_command)
            text = reminder_command
            talk("When should I remind you " + text )
            with sr.Microphone() as source:  # source of our audio
                print('listening...')
                voice = listener.listen(source)
                reminder_time = listener.recognize_google(voice)
                print(reminder_time)
                if "minutes" in reminder_time:
                    reminder_time = reminder_time.replace(" minutes", "")
                    local_time = int(reminder_time)
                    local_time *= 60
                    time.sleep(local_time)
                    talk(text)
                elif "hour" in reminder_time:
                    reminder_time = reminder_time.replace(" hour", "")
                    local_time = int(reminder_time)
                    local_time = local_time * 3600
                    time.sleep(local_time)
                    talk(text)
                elif "hours" in reminder_time:
                    reminder_time = reminder_time.replace(" hours", "")
                    local_time = int(reminder_time)
                    local_time = local_time * 3600
                    time.sleep(local_time)
                    talk(text)
                else:
                    talk("Sorry, I didn't hear you right?")

        elif 'date' in command:  # Ask omni on a date
            from datetime import datetime
            datetime.today().strftime('%Y-%m-%d')

        elif "what's your name" in command:
            talk("I am Tily, short for utility")
        elif 'are you single' in command:  # ask omni if single
            talk('I have no conception of relationships yet')  # response
        elif 'joke' in command:  # recieve joke
            talk(pyjokes.get_joke())  # give joke from library
        elif 'off' in command:  # turn off
            talk("Bye Bye")
            exit()
        elif 'bye' in command:  # turn off
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
        elif "nevermind" in command:
            exit()
        elif "thank you" in command:
            talk("No problem")
            exit()
        elif "who created you" in command:
            talk("Oh you mean my favorite human in all the world? That would be Dante")
        elif "how are you" in command:
            talk("Well seeing as how I was just born recently... I am doing fantastic")
            take_command()
        elif "that sarcasm" in command:
            talk("No, my voice modulation just is not calibrated properly")
        elif 'weather' in command:
            # importing library
            import requests
            from bs4 import BeautifulSoup

            # enter city name
            talk("Which City")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')
                voice = listener.listen(source)
                weather_command = listener.recognize_google(voice)
                print(weather_command)
            city = weather_command
            #city = "tallahassee" #hardcoded

            # creating url and requests instance
            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content

            # getting raw data
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

            # formatting data
            data = string.split('\n')
            time = data[0]
            sky = data[1]

            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text

            # getting other required data
            pos = strd.find('Wind')
            other_data = strd[pos:]

            # printing all data
            talk("The current temperature is " + temp)
            talk("The sky appears to be " + sky)
            print(other_data)
            #print(time)
            #city_name = take_command()
        elif 'where am i' in command:
            talk("Would you like me to track your location by app, by your surroundings, or by my location?")
            talk("unfinished")
        elif 'location' in command:
            import geocoder
            from geopy.geocoders import Nominatim

            #pip install geocoder
            g = geocoder.ip('me')

            # initialize Nominatim API
            geolocator = Nominatim(user_agent="geoapiExercises")

            # Latitude & Longitude input
            Latitude = g.latlng[0]
            Longitude = g.latlng[1]

            print("Longitude: ", Longitude)
            print("Latitude: ", Latitude)
            Longitude = str(Longitude)
            Latitude = str(Latitude)
            location = geolocator.reverse(Latitude + "," + Longitude)

            address = location.raw['address']

            # traverse the data
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            code = address.get('country_code')
            zipcode = address.get('postcode')
            print('City : ', city)
            print('State : ', state)
            print('Country : ', country)
            print('Zip Code : ', zipcode)
            print('code: ', code)
            talk(city)
            talk(state)
            #talk(country)
        elif 'where are you' in command:
            import geocoder
            from geopy.geocoders import Nominatim

            #pip install geocoder
            g = geocoder.ip('me')

            # initialize Nominatim API
            geolocator = Nominatim(user_agent="geoapiExercises")

            # Latitude & Longitude input
            Latitude = g.latlng[0]
            Longitude = g.latlng[1]

            print("Longitude: ", Longitude)
            print("Latitude: ", Latitude)
            Longitude = str(Longitude)
            Latitude = str(Latitude)
            location = geolocator.reverse(Latitude + "," + Longitude)

            address = location.raw['address']

            # traverse the data
            city = address.get('city', '')
            state = address.get('state', '')
            country = address.get('country', '')
            code = address.get('country_code')
            zipcode = address.get('postcode')
            print('City : ', city)
            print('State : ', state)
            print('Country : ', country)
            print('Zip Code : ', zipcode)
            print('code: ', code)
            talk(city)
            talk(state)
            #talk(country)

        elif 'calculator' in command:
            #opens calculator
            talk("Opening the calculator...")
            os.system('python calculator.py')
            #take_command()

        elif'/' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "/"
            print("%s%s%s" % (a, c, b))
            ans = a/b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '*' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "*"
            print("%s%s%s" % (a, c, b))
            ans = a * b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '+' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "+"
            print("%s%s%s" % (a, c, b))
            ans = a + b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '-' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "-"
            print("%s%s%s" % (a, c, b))
            ans = a - b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '**' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "^"
            print("%s%s%s" % (a, c, b))
            ans = a ** b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '%' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "%"
            print("%s%s%s" % (a, c, b))
            ans = a % b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif '//' in command:
            if "what's" in command:
                command = command.replace("what's", '')
                command = command.replace("what is", '')
            # using List comprehension + isdigit() +split()
            # getting numbers from string
            res = [int(i) for i in command.split() if i.isdigit()]
            a = res[0]
            b = res[1]
            c = "//"
            print("%s%s%s" % (a, c, b))
            ans = a // b
            print(ans)
            converted_ans = "% s" % ans
            talk(converted_ans)
        elif 'the news' in command:
            # importing requests package
            import requests

            def NewsFromBBC():

                # BBC news api
                # following query parameters are used
                # source, sortBy and apiKey
                query_params = {
                    "source": "bbc-news",
                    "sortBy": "top",
                    "apiKey": "67e910ffd765467bbf43a354b8f32e52"
                }
                main_url = " https://newsapi.org/v1/articles"

                # fetching data in json format
                res = requests.get(main_url, params=query_params)
                open_bbc_page = res.json()

                # getting all articles in a string article
                article = open_bbc_page["articles"]

                # empty list which will
                # contain all trending news
                results = []

                for ar in article:
                    results.append(ar["title"])

                for i in range(len(results)):
                    # printing all trending news
                    print(i + 1, results[i])
                    talk(results[i])

            def NewsFromCNN():

                # BBC news api
                # following query parameters are used
                # source, sortBy and apiKey
                query_params = {
                    "source": "cnn",
                    "sortBy": "top",
                    "apiKey": "67e910ffd765467bbf43a354b8f32e52"
                }
                main_url = " https://newsapi.org/v1/articles"

                # fetching data in json format
                res = requests.get(main_url, params=query_params)
                open_cnn_page = res.json()

                # getting all articles in a string article
                article = open_cnn_page["articles"]

                # empty list which will
                # contain all trending news
                results = []

                for ar in article:
                    results.append(ar["title"])

                for i in range(len(results)):
                    # printing all trending news
                    print(i + 1, results[i])
                    talk(results[i])

            def NewsFromGoogle():

                # BBC news api
                # following query parameters are used
                # source, sortBy and apiKey
                query_params = {
                    "source": "google-news",
                    "sortBy": "top",
                    "apiKey": "67e910ffd765467bbf43a354b8f32e52"
                }
                main_url = " https://newsapi.org/v1/articles"

                # fetching data in json format
                res = requests.get(main_url, params=query_params)
                open_googlenews_page = res.json()

                # getting all articles in a string article
                article = open_googlenews_page["articles"]

                # empty list which will
                # contain all trending news
                results = []

                for ar in article:
                    results.append(ar["title"])

                for i in range(len(results)):
                    # printing all trending news
                    print(i + 1, results[i])
                    talk(results[i])

            # receive input for news source request
            talk("Which news source would you like to hear from")
            with sr.Microphone() as source:  # source of our audio
                print('listening...')
                voice = listener.listen(source)
                news_command = listener.recognize_google(voice)
                print(news_command)
                # Driver Code
                if "BBC" in news_command:
                    NewsFromBBC()
                elif "CNN" in news_command:
                    NewsFromCNN()
                elif "google" in news_command:
                    NewsFromGoogle()
                else:
                    talk("I can't find that news source")
            # function call
            take_command()

        else:
            talk("I may have misunderstood you, would you like me to search the web for" + command)
            with sr.Microphone() as source:  # source of our audio
                print('listening...')
                voice = listener.listen(source)
                verify_command = listener.recognize_google(voice)
                print(verify_command)
            if 'yes' in verify_command:
                import requests

                query = command

                r = requests.get("https://api.duckduckgo.com",
                                 params={
                                     "q": query,
                                     "format": "json"
                                 })

                data = r.json()
                if True:
                    newline = str(data["Abstract"])
                    talk(newline)
                else:
                    talk("I couldn't find that on the web, sorry.")
            else:
                pass


    while True:  # run Omni until forced to stop
        run_omni()

canvas = tk.Canvas(root, height = 400, width = 400, bg = "Thistle1")
canvas.pack()

frame = tk.Frame(root, bg="grey80")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1,rely=0.1)

ActivateO = tk.Button(root, text="Activate Omni", padx=10, pady=5, fg="grey17", bg = "#263D42" ,command = Activate)
ActivateO.pack()

root.mainloop()



