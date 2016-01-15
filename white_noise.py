#!/usr/bin/python

import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def main():
    pygame.init()
    # Load the sound to play indefinitely
    pygame.mixer.music.load('white_noise.ogg')
    pygame.mixer.music.play(-1)
    # Pause the sound
    pygame.mixer.music.pause()
    paused = True

    # Poll button and toggle pausing
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            if paused:
                pygame.mixer.music.unpause()
                paused = False
                time.sleep(1)
                print paused
            else:
                pygame.mixer.music.pause()
                paused = True
                time.sleep(1)
                print paused


if __name__ == '__main__':
    main()
