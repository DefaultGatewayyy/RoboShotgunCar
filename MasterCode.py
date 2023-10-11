'''python code'''
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
'''Dette specificerer RPi pins til at følge "Broadcom SOC channel"... Aka., det definere pins i en bestemt rækkefølge'''


RWheel1 = 13
RWheelDir1 = 4
RWheel2 = 19
RWheelDir2 = 17

LWheel1 = 18
LWheelDir1 = 23
LWheel2 = 12
LWheelDir2 = 22
'''Dette er midlertidige pins. Vi skal have sat dem til det de rigtigt skal være...'''

GPIO.setup(RWheel1, GPIO.OUT)
GPIO.setup(RWheelDir1, GPIO.OUT)
GPIO.setup(RWheel2, GPIO.OUT)
GPIO.setup(RWheelDir2, GPIO.OUT)

GPIO.setup(LWheel1, GPIO.OUT)
GPIO.setup(LWheelDir1, GPIO.OUT)
GPIO.setup(LWheel2, GPIO.OUT)
GPIO.setup(LWheelDir2, GPIO.OUT)



def RWheel1_Dir(i):
    GPIO.output(RWheelDir1, i)
def RWheel2_Dir(i):
    GPIO.output(RWheelDir2, i)
def LWheel1_Dir(i):
    GPIO.output(LWheelDir1, i)
def LWheel2_Dir(i):
    GPIO.output(LWheelDir2, i)
'''Dette siger hvilken retning som hjulene skal dreje...'''


def RWheel1_Speed(i):
    GPIO.output(RWheel1, i)
def RWheel2_Speed(i):
    GPIO.output(RWheel2, i)
def LWheel1_Speed(i):
    GPIO.output(LWheel1, i)
def LWheel2_Speed(i):
    GPIO.output(LWheel2, i)
'''Dette siger hvilken hastighed hjulene skal have...'''


RWheel1_Dir(True)
RWheel1_Speed(100)

RWheel2_Dir(True)
RWheel2_Speed(100)

LWheel1_Dir(True)
LWheel1_Speed(100)

LWheel2_Dir(True)
LWheel2_Speed(100)


'''
pi_pwm_Front1 = GPIO.PWM(FrontWheel1, 1000)
pi_pwm_Front1.start(0)
pi_pwm_Front2 = GPIO.PWM(FrontWheel2, 1000)
pi_pwm_Front2.start(0)

pi_pwm_Back1 = GPIO.PWM(BackWheel1, 1000)
pi_pwm_Back1.start(0)
pi_pwm_Back2 = GPIO.PWM(BackWheel2, 1000)
pi_pwm_Back2.start(0)
'''
'''Dette instiller hastighed på hjulene'''