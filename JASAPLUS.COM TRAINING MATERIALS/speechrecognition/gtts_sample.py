#!/usr/bin/env python3
from gtts import gTTS
'''
gtts_sample.py
'''
import os
words = 'Saya lapar sekali'
tts = gTTS(text= words, lang='id', slow=True).save("tmp.mp3")
cmd = "vlc --intf dummy tmp.mp3 vlc://quit"
pipe = os.popen(cmd).read()
print (pipe)
