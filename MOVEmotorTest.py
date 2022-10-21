from time import sleep
#import MOVEmotorV1_2 as MOVEmotor
import MOVEmotorV3 as MOVEmotor

MOVEmotor.setupMotorDriver()

while 1:
    MOVEmotor.LeftMotor(255)
    sleep(0.5)
    MOVEmotor.RightMotor(255)
    sleep(0.5)
    MOVEmotor.StopMotors()
    sleep(0.5)
