# test_gpio.py
import RPi.GPIO as GPIO
import time

pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

try:
    print("Turning ON GPIO", pin)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
    print("Turning OFF GPIO", pin)
    GPIO.output(pin, GPIO.LOW)
finally:
    GPIO.cleanup()
