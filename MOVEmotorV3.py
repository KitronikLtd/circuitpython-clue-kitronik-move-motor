from time import sleep
import board
import neopixel

ws2811 = neopixel.NeoPixel(board.P12, 2)

def setupMotorDriver():
    pass

def LeftMotor(speed):
    speed = int(speed)
    if(speed > 255):
        speed = 255
    elif(speed < -255):
        speed = -255
    m = bytearray(3)
    mJ = bytearray(3)
    if(speed > 0):
        #going forwards
        m[0] = speed
        m[1] = 0
        mJ[0] = 255
        mJ[1] = 0
    else:
        #going backwards, or stopping
        m[0] = 0
        m[1] = speed * -1
        mJ[0] = 0
        mJ[1] = 255
    if speed == 0:
        m[2] = 255
    else:
        m[2] = 0
        ws2811[1] = (mJ[0], mJ[1], mJ[2])
        ws2811.show()
        sleep(1)
    ws2811[1] = (m[0], m[1], m[2])
    ws2811.show()

#speed -255 -> +255
def RightMotor(speed):
    speed = int(speed)
    if(speed > 255):
        speed = 255
    elif(speed < -255):
        speed = -255
    m = bytearray(3)
    mJ = bytearray(3)
    if(speed > 0):
        #going forwards
        m[0] = 0
        m[1] = speed
        mJ[0] = 0
        mJ[1] = 255
    else:
        #going backwards, or stopping
        m[0] = speed * -1
        m[1] = 0
        mJ[0] = 255
        mJ[1] = 0
    if speed == 0:
        m[2] = 255
    else:
        m[2] = 0
        ws2811[0] = (mJ[0], mJ[1], mJ[2])
        ws2811.show()
        sleep(1)
    ws2811[0] = (m[0], m[1], m[2])
    ws2811.show()

#A function that stops both motors, rather than having to call Left and Right with zero speed.
def StopMotors():
    LeftMotor(0)
    RightMotor(0)

