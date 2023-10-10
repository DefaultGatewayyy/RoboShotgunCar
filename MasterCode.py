'''python code'''
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
'''Dette specificerer RPi pins til at følge "Broadcom SOC channel"... Aka., det definere pins i en bestemt rækkefølge'''


FrontWheel1 = 1
FrontWheelDir1 = 2
FrontWheel2 = 3
FrontWheelDir2 = 4

BackWheel1 = 5
BackWheelDir1 = 6
BackWheel2 = 7
BackWheelDir2 = 8
'''Dette er midlertidige pins. Vi skal have sat dem til det de rigtigt skal være...'''


GPIO.output(FrontWheelDir1, True)
GPIO.output(FrontWheelDir2, True)
GPIO.output(BackWheelDir1, True)
GPIO.output(BackWheelDir2, True)
'''Dette siger hvilken retning som hjulene skal dreje...'''


pi_pwm_Front1 = GPIO.PWM(FrontWheel1, 1000)
pi_pwm_Front1.start(0)
pi_pwm_Front2 = GPIO.PWM(FrontWheel2, 1000)
pi_pwm_Front2.start(0)

pi_pwm_Back1 = GPIO.PWM(BackWheel1, 1000)
pi_pwm_Back1.start(0)
pi_pwm_Back2 = GPIO.PWM(BackWheel2, 1000)
pi_pwm_Back2.start(0)
'''Dette instiller hastighed på hjulene'''