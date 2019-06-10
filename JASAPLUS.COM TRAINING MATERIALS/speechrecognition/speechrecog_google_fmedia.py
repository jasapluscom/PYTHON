#!/usr/bin/env python3
import speech_recognition as sr
import time, os
AUDIO_FILE = "mono.flac"

while True:
    try:
        os.system("rm mono.flac")
        os.system("fmedia --dev-capture=2 --volume=98 --channels=mono --rate=16000 --record -o mono.flac --until=4")
        '''
        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            res =  r.recognize_google(audio)
            #os.system("espeak -ven-us+f5 -s 100 '"+res+"' --stdout |  aplay -D 'default'")
            os.system("espeak -ven-us+f5 -s 100 '"+res+"'")
        '''
    except:
        print("error")
        pass
