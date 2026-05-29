import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

STEP2=17
DIR2=27
EN2=22
STEP=5
DIR=6
EN=26
STEP3=14
DIR3=15
EN3=18
pins=[STEP,DIR,EN,STEP2,DIR2,EN2,STEP3,DIR3,EN3]
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
GPIO.output(EN,GPIO.LOW)
GPIO.output(EN2,GPIO.LOW)
GPIO.output(EN3,GPIO.LOW)
GPIO.output(DIR,GPIO.HIGH)
GPIO.output(DIR2,GPIO.HIGH)
GPIO.output(DIR3,GPIO.HIGH)
STEPS_PER_REV=1600
def rotate(degrees,speed=0.003):
    direction = 1 if degrees >= 0 else -1
    steps=int((abs(degrees)/360.0)*STEPS_PER_REV)
    GPIO.output(DIR,GPIO.LOW if direction == 1 else GPIO.HIGH)
    #GPIO.output(DIR2,GPIO.LOW if direction2 == 1 else GPIO.HIGH)
    for _ in range(steps):
        GPIO.output(STEP,GPIO.HIGH)
        #GPIO.output(STEP2,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STEP,GPIO.LOW)
        #GPIO.output(STEP2,GPIO.LOW)
        time.sleep(0.001)
def rotate2(degrees,speed=0.003):
    direction = 1 if degrees >= 0 else -1
    steps=int((abs(degrees)/480.0)*STEPS_PER_REV)
    GPIO.output(DIR2,GPIO.LOW if direction == 1 else GPIO.HIGH)
    for _ in range(steps):
        GPIO.output(STEP2,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STEP2,GPIO.LOW)
        time.sleep(0.001)

def rotate3(degrees,speed=0.003):
    direction = 1 if degrees >= 0 else -1
    steps=int((abs(degrees)/360.0)*STEPS_PER_REV)
    GPIO.output(DIR3,GPIO.LOW if direction == 1 else GPIO.HIGH)
    #GPIO.output(DIR2,GPIO.LOW if direction2 == 1 else GPIO.HIGH)
    for _ in range(steps):
        GPIO.output(STEP3,GPIO.HIGH)
        #GPIO.output(STEP2,GPIO.HIGH)
        time.sleep(0.0001)
        GPIO.output(STEP3,GPIO.LOW)
        #GPIO.output(STEP2,GPIO.LOW)
        time.sleep(0.0001)

try:
    while True:
        #deg=float(input("Enter degrees to rotate: "))
        deg2 = float(input("Enter degrees to rotate: "))
        #deg3 = float(input("Enter degrees to rotate: "))
        #rotate(deg)
        rotate2(deg2)
        #rotate3(deg3)
        print("finishing rotation")
       
except KeyboardInterrupt:
    GPIO.cleanup()