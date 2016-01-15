#!/usr/bin/python

import RPi.GPIO as GPIO
import pygame
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
    # Pause the sound
    paused = True
    script_dir = os.path.dirname(__file__)

    # Poll button and toggle pausing
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            if paused:
                pygame.init()
                # Load the sound to play indefinitely
                sound_file = 'white_noise.ogg'
                pygame.mixer.music.load(os.path.join(script_dir, sound_file))
                pygame.mixer.music.play(-1)
                paused = False
                time.sleep(1)
            else:
                pygame.quit()
                paused = True
                time.sleep(1)


if __name__ == '__main__':
    main()
