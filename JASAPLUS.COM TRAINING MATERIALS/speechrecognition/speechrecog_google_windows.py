#!/usr/bin/env python3
'''
speechrecog_google_windows.py
sample for python training
at jasaplus.com
'''

import speech_recognition as sr
import time, os
AUDIO_FILE = "mono.flac"

while True:
    try:
        os.system("del mono.flac")
        os.system("fmedia --dev-capture=2 --volume=98 --channels=mono --rate=16000 --record -o mono.flac --until=5")
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            res =  r.recognize_google(audio)
            print(res)
            #os.system("espeak -ven-us+f5 -s 100 '"+res+"' --stdout |  aplay -D 'default'")
            os.system('espeak -ven-us+f5 -s 100 "' +res+ '"')
            time.sleep(1)
    except:
        print("error")
        pass

