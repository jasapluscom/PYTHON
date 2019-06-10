#!/usr/bin/env python3
'''
speechrecog_google.py
for python training at jasaplus.com
'''
import speech_recognition as sr
import os
AUDIO_FILE = "tmp.flac"
r = sr.Recognizer()
while True:
    try:
        os.system("AUDIODEV=plughw:1,0 rec --channels=1 --bits=24 --rate=44100 tmp.flac trim 0 5")
        with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            res =  r.recognize_google(audio)
            print("\n" + res + "\n")
            os.system("espeak -ven-us+f5 -s 100 '"+res+"'")
    except Exception as e:
        print(e)
        pass
