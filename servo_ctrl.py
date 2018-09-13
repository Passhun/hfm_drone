import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

gp_out = 17

GPIO.setup(gp_out, GPIO.OUT)

servo = GPIO.PWM(gp_out,50)

servo.start(1)
#time.sleep(1)

for i in range(3):

#	servo.ChangeDutyCycle(2.5)
#	time.sleep(0.5)

	servo.ChangeDutyCycle(7.25)
	time.sleep(0.2)

	servo.stop()

#        servo.ChangeDutyCycle(12)
#        time.sleep(0.5)

#        servo.ChangeDutyCycle(7.25)
#        time.sleep(0.5)
	servo.start(1)
        servo.ChangeDutyCycle(5)
#	servo.stop()
        time.sleep(0.5)

#        servo.ChangeDutyCycle(2.5)
#        time.sleep(0.5)


servo.stop()
GPIO.cleanup()


	
