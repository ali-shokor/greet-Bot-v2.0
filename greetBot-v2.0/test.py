# test.py
import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load and play sound
pygame.mixer.music.load("sounds/greeting/welcome1.wav")  # Put any .wav/.mp3 here
pygame.mixer.music.play()

# Wait for the sound to finish playing
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
