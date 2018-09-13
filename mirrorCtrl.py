import RPi.GPIO as GPIO
import time
import sys

argv = sys.argv

slope1 = 475
slope2 = 90
Seg = 725
angle = argv[1]

duty = float(slope1*int(angle)/slope2+Seg)/100

print (angle)
print (duty)

GPIO.setmode(GPIO.BCM)

gp_out = 17

GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out,50)

servo.start(1)
#time.sleep(1)

servo.ChangeDutyCycle(duty)
time.sleep(0.2)

servo.stop()
GPIO.cleanup()


	
