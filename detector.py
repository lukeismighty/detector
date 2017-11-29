#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import vlc
import os

# Set my variables for their pins
magnetSensor = 11

# Set the audio to not be on full and assign an audio file
os.system('amixer set Master 100%')
audioFile = "/home/pi/Desktop/detector/Bird_in_Rain-Mike_Koenig-441535833.mp3"

# Create an instance of the media player with the audio file
audio = vlc.MediaPlayer(audioFile)

# Set the GPIO warnings to mute and the GPIO to use physical pin counts
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(magnetSensor, GPIO.IN) # (for pirSensor)
GPIO.setup(magnetSensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # (for reedSwitch)

print GPIO.input(magnetSensor)

try:
  while True:
    currentStatus = GPIO.input(magnetSensor)
    if currentStatus == 1:
      print "Door ajar."
    if currentStatus == 0:
      time.sleep(0.1)
    elif currentStatus == 1:
      # Start playing the audio sound
      audio.play()
      time.sleep(4)

    # Stop playing the audio sound
    audio.stop()

finally:
  GPIO.cleanup()
