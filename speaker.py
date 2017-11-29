import os

from time import sleep

def playMusic():
    sleep(1)
    os.system('mpg123 Stemtest.mp3')

playMusic()

