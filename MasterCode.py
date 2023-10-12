'''python code'''
import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BCM)
'''Dette specificerer RPi pins til at følge "Broadcom SOC channel"... Aka., det definere pins i en bestemt rækkefølge'''

GPIO.cleanup()

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



def RWheel1_Dir(i):
    GPIO.output(RWheelDir1, i)
def RWheel2_Dir(i):
    GPIO.output(RWheelDir2, i)
def LWheel1_Dir(i):
    GPIO.output(LWheelDir1, i)
def LWheel2_Dir(i):
    GPIO.output(LWheelDir2, i)
'''Dette siger hvilken retning som hjulene skal dreje...'''



RWheel1_Dir(False)
RWheel2_Dir(False)

LWheel1_Dir(False)
LWheel2_Dir(False)

PWM_RWheel1.ChangeDutyCycle(100)



while True:
    if GPIO.input(SensorR) == 1 and GPIO.input(SensorL) == 1:
        PWM_RWheel1.ChangeDutyCycle(100)
        PWM_RWheel2.ChangeDutyCycle(100)
        PWM_LWheel1.ChangeDutyCycle(100)
        PWM_LWheel2.ChangeDutyCycle(100)
    
    elif GPIO.input(SensorR) == 1 and GPIO.input(SensorL) == 0:
        PWM_RWheel1.ChangeDutyCycle(0)
        PWM_RWheel2.ChangeDutyCycle(0)
        PWM_LWheel1.ChangeDutyCycle(50)
        PWM_LWheel2.ChangeDutyCycle(50)

    elif GPIO.input(SensorR) == 0 and GPIO.input(SensorL) == 1:
        PWM_RWheel1.ChangeDutyCycle(50)
        PWM_RWheel2.ChangeDutyCycle(50)
        PWM_LWheel1.ChangeDutyCycle(0)
        PWM_LWheel2.ChangeDutyCycle(0)
