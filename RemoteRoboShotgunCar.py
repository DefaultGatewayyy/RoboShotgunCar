
'''python code'''
import RPi.GPIO as GPIO
from time import sleep
from sshkeyboard import listen_keyboard



GPIO.setmode(GPIO.BCM)
'''Dette specificerer RPi pins til at følge "Broadcom SOC channel"... Aka., det definere pins i en bestemt rækkefølge'''


'''
left front = RWheel1
left back = RWheel2
right back = LWheel1
right fron = LWheel2

'''

LWheel1 = 13
RWheelDir1 = 4
LWheel2 = 19
RWheelDir2 = 17

RWheel2 = 18
LWheelDir1 = 23
RWheel1 = 12
LWheelDir2 = 22
'''Dette er midlertidige pins. Vi skal have sat dem til det de rigtigt skal være...'''

SensorR = 24
SensorL = 25
'''Sensor pins'''


GPIO.setup(RWheel1, GPIO.OUT)
GPIO.setup(RWheelDir1, GPIO.OUT)
GPIO.setup(RWheel2, GPIO.OUT)
GPIO.setup(RWheelDir2, GPIO.OUT)

GPIO.setup(LWheel1, GPIO.OUT)
GPIO.setup(LWheelDir1, GPIO.OUT)
GPIO.setup(LWheel2, GPIO.OUT)
GPIO.setup(LWheelDir2, GPIO.OUT)
'''Motor pins bliver sat til output, da de skal have data vi giver dem'''

GPIO.setup(SensorR, GPIO.IN)
GPIO.setup(SensorL, GPIO.IN)
'''Sensor pins bliver sat til input, da vi skal bruge data de giver os'''



PWM_RWheel1 = GPIO.PWM(RWheel1, 1000)
PWM_RWheel1.start(0)
PWM_RWheel2 = GPIO.PWM(RWheel2, 1000)
PWM_RWheel2.start(0)

PWM_LWheel1 = GPIO.PWM(LWheel1, 1000)
PWM_LWheel1.start(0)
PWM_LWheel2 = GPIO.PWM(LWheel2, 1000)
PWM_LWheel2.start(0)
'''Her sætter vi alle "Wheels" op til at køre med pwm'''



def Wheel_Dir(i):
    GPIO.output(RWheelDir1, i)
    GPIO.output(RWheelDir2, i)
    GPIO.output(LWheelDir1, i)
    GPIO.output(LWheelDir2, i)
'''Dette siger hvilken retning som hjulene skal dreje...'''



def TurnLeft():
    Wheel_Dir(False)
    PWM_RWheel1.ChangeDutyCycle(45)
    PWM_RWheel2.ChangeDutyCycle(45)
    PWM_LWheel1.ChangeDutyCycle(0)
    PWM_LWheel2.ChangeDutyCycle(0)

def TurnRight():
    Wheel_Dir(False)
    PWM_RWheel1.ChangeDutyCycle(0)
    PWM_RWheel2.ChangeDutyCycle(0)
    PWM_LWheel1.ChangeDutyCycle(45)
    PWM_LWheel2.ChangeDutyCycle(45)

def GoForward():
    Wheel_Dir(False)
    PWM_RWheel1.ChangeDutyCycle(120)
    PWM_RWheel2.ChangeDutyCycle(120)
    PWM_LWheel1.ChangeDutyCycle(120)
    PWM_LWheel2.ChangeDutyCycle(120)

def GoBackward():
    Wheel_Dir(True)
    PWM_RWheel1.ChangeDutyCycle(45)
    PWM_RWheel2.ChangeDutyCycle(45)
    PWM_LWheel1.ChangeDutyCycle(45)
    PWM_LWheel2.ChangeDutyCycle(45)

def Stop():
    PWM_RWheel1.ChangeDutyCycle(0)
    PWM_RWheel2.ChangeDutyCycle(0)
    PWM_LWheel1.ChangeDutyCycle(0)
    PWM_LWheel2.ChangeDutyCycle(0)

def TurnAndRunLeft():
    PWM_RWheel1.ChangeDutyCycle(110)
    PWM_RWheel2.ChangeDutyCycle(110)
    PWM_LWheel1.ChangeDutyCycle(90)
    PWM_LWheel2.ChangeDutyCycle(90)

def press(key):
    if key == "w":
        GoForward()
    if key == "s":
        GoBackward()
    if key == "a":
        TurnLeft()
    if key == "d":
        TurnRight()
    if key == "w" and key == "a":
        TurnAndRunLeft()

def release(key):
    if key == "w" or key == "s" or key == "a" or key == "d" or key == "w" and key == "a":
        Stop()

while True:
    listen_keyboard(on_press = press, on_release = release)
