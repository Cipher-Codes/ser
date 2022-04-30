import nltk

nltk.data.path.append('C:\\Users\\pocob\\AppData\\Roaming\\nltk_data')


from nrclex import NRCLex

import speech_recognition as sr


# initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Recognizing...")

    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)





#text = "I hate to visit the historical places"

emotions = NRCLex(text)

print(emotions.top_emotions)
