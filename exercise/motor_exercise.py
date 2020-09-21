import RPi.GPIO as GPIO
import time

STOP = 0
FORWARD = 1
BACKWARD = 2

CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0

ENA = 26 #board 37 pin
ENB = 0 #board 27 pin

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5

def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    pwm = GPIO.PWM(EN, 100)
    pwm.start(0)
    return pwm

def setMotorControl(pwm, INA, INB, speed, stat):
    pwm.ChangeDutyCycle(speed)
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorControl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorControl((pwmB, IN3, IN4, speed, stat))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

setMotor(CH1, 50, FORWARD)
setMotor(CH2, 50, FORWARD)
time.sleep(5)

setMotor(CH1, 50, BACKWARD)
setMotor(CH2, 50, BACKWARD)
time.sleep(5)

setMotor(CH1, 50, FORWARD)
setMotor(CH2, 20, FORWARD)
time.sleep(5)

setMotor(CH1, 20, FORWARD)
setMotor(CH2, 50, FORWARD)
time.sleep(5)

setMotor(CH1, 50, STOP)
setMotor(CH2, 50, STOP)
time.sleep(5)