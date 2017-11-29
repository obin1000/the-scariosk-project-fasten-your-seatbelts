import os
from time import sleep

playMusic()

def playMusic():

    sleep(1)
    os.system('mpg123 -q ')

