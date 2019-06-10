#!/usr/bin/env python3
'''
speech_indo.py
for python training at jasaplus.com
'''
import speech_recognition as sr
import os
from gtts import gTTS
AUDIO_FILE = "tmp.flac"
r = sr.Recognizer()
while True:
    try:
        os.system("AUDIODEV=plughw:1,0 rec --channels=1 --bits=24 --rate=44100 tmp.flac trim 0 5")
        with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            res =  r.recognize_google(audio, language='ID')
            print("\n" + res + "\n")
            tts = gTTS(text= res, lang='id', slow=True).save("tmp.mp3")
            cmd = "mpg123 tmp.mp3"
            pipe = os.popen(cmd).read()
            print (pipe)
    except Exception as e:
        print(e)
        pass
