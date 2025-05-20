import RPi.GPIO as GPIO

LEFT_FORWARD = 19
LEFT_BACKWARD = 26
RIGHT_FORWARD = 6
RIGHT_BACKWARD = 13
MOTOR_PINS = [LEFT_FORWARD, LEFT_BACKWARD, RIGHT_FORWARD, RIGHT_BACKWARD]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Defer setup into a function to control timing
def init_motors():
    for pin in MOTOR_PINS:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def stop():
    for pin in MOTOR_PINS:
        GPIO.output(pin, GPIO.LOW)

def forward():
    stop()
    GPIO.output(LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_FORWARD, GPIO.HIGH)

def backward():
    stop()
    GPIO.output(LEFT_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_BACKWARD, GPIO.HIGH)

def left():
    stop()
    GPIO.output(LEFT_BACKWARD, GPIO.HIGH)
    GPIO.output(RIGHT_FORWARD, GPIO.HIGH)

def right():
    stop()
    GPIO.output(LEFT_FORWARD, GPIO.HIGH)
    GPIO.output(RIGHT_BACKWARD, GPIO.HIGH)
