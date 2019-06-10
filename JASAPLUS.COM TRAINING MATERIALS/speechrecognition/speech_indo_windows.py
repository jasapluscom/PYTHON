#!/usr/bin/env python3
'''
speech_indo_windows.py
for python training at jasaplus.com
'''
import speech_recognition as sr
import os
from gtts import gTTS
AUDIO_FILE = "mono.flac"
r = sr.Recognizer()
while True:
    try:
        os.system("del mono.flac")
        os.system("fmedia --dev-capture=2 --volume=98 --channels=mono --rate=16000 --record -o mono.flac --until=5")
        with sr.AudioFile(AUDIO_FILE) as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
            res =  r.recognize_google(audio, language='ID')
            print("\n" + res + "\n")
            tts = gTTS(text= res, lang='id', slow=True).save("tmp.mp3")
            cmd = "vlc --intf dummy tmp.mp3 vlc://quit"
            pipe = os.popen(cmd).read()
            print (pipe)
    except Exception as e:
        print(e)
        pass
