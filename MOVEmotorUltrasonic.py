# A 'free roaming' robot example for Adafruit CLUE on Kitronik :MOVE motor buggy chassis.
# Uses the ultrasonic to detect an obstacle and indicates a range using the LEDs
# If something is close and in the way then stop, beep the horn and turn away

import board
import digitalio
import pulseio
from time import sleep
import neopixel
import busio
import adafruit_hcsr04
import math
from random import randint
#import MOVEmotorV1_2 as MOVEmotor
import MOVEmotorV3 as MOVEmotor

MOVEmotor.setupMotorDriver();
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.P13, echo_pin = board.P14)
pixels = neopixel.NeoPixel(board.P8,4)

#define some colours to make life easier
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255,255)

#wrapper for the sonar to have try in. On error we will report a very short distance
def GetDistance():
    try:
        value = sonar.distance
    except RuntimeError:
        value =  1.0
    return value

def BeepHorn():
    #a beep beep
    buzzer = pulseio.PWMOut(board.P0,duty_cycle=2 ** 15, frequency=500, variable_frequency=True)
    sleep(0.5)
    buzzer.deinit()
    sleep(0.1)
    buzzer = pulseio.PWMOut(board.P0,duty_cycle=2 ** 15, frequency=500, variable_frequency=True)
    sleep(0.5)
    buzzer.deinit()

#now loop doingt hemain code.
while True:
    distance = GetDistance()
    print("Distance", distance)

    if distance > 10:
        MOVEmotor.LeftMotor(100)
        MOVEmotor.RightMotor(100)
        pixels.fill(GREEN)

    elif distance == 0:
        MOVEmotor.StopMotors()
        pixels.fill(RED)
        BeepHorn()

    elif distance < 10:
        MOVEmotor.StopMotors()
        sleep(0.5)
        MOVEmotor.LeftMotor(-50)
        MOVEmotor.RightMotor(-50)
        pixels.fill(WHITE)
        sleep(0.5)
        random = randint(0, 1)
        if random == 0:
            MOVEmotor.LeftMotor(50)
            MOVEmotor.RightMotor(-50)
            pixels.fill(BLUE)
        else:
            MOVEmotor.LeftMotor(-50)
            MOVEmotor.RightMotor(50)
            pixels.fill(BLUE)
        sleep(0.5)
        MOVEmotor.StopMotors()


