# Example code for using Clue on Kitronik MOVE motor using CircuitPython
To use, save MOVEmotorV1_2.py file onto the Clue if you have a Kitronik MOVE motor V1 to V2.
To use, save MOVEmotorV3.py file onto the Clue if you have a Kitronik MOVE motor V3.
## Import MOVEmotor and run setup:
```python
    import MOVEmotorV1_2 as MOVEmotor
    import MOVEmotorV3 as MOVEmotor
    MOVEmotor.setupMotorDriver()
 ```
## Motors
### Drive motors:
```python
    MOVEmotor.LeftMotor(speed)
    MOVEmotor.RightMotor(speed)
```
where:
* speed => -255 to 255

### Stop motors:
```python
    MOVEmotor.StopMotors()
```
## Ultrasonic Sensor
```python
    sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.P13, echo_pin = board.P14)
    def GetDistance():
        try:
            value = sonar.distance
        except RuntimeError:
            value =  1.0
        return value
```