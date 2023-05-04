import os
import pyttsx3

engine = pyttsx3.init()
engine.say("Your computer is hacked")
engine.runAndWait()

os.system("shutdown /s /t 2")