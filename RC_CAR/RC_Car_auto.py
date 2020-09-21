import RPi.GPIO as GPIO
import time
#motor_code
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

#ultrasonic_code
frt_trig = 8 #pin24
frt_echo = 25 #pin 22

back_trig = 22 #pin15
back_echo = 27 #pin13

rig_trig = 1 #pin28
rig_echo = 7 #pin26

left_trig = 9 #pin21
left_echo = 10 #pin19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(frt_trig , GPIO.OUT)
GPIO.setup(rig_trig , GPIO.OUT)
GPIO.setup(left_trig , GPIO.OUT)
GPIO.setup(back_trig , GPIO.OUT)

GPIO.setup(frt_echo , GPIO.IN)
GPIO.setup(rig_echo , GPIO.IN)
GPIO.setup(left_echo , GPIO.IN)
GPIO.setup(back_echo , GPIO.IN)

#motor_function
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
        setMotorControl(pwmB, IN3, IN4, speed, stat)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

#ultrasonic function
def dist(trig, echo):
    global  str, end
    GPIO.output(trig, False)
    time.sleep(0.5)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0:
        srt = time.time()
    while GPIO.input(echo) == 1:
        end = time.time()

    puls_drtn = end-srt
    distance = puls_drtn * 17000
    distance = round(distance, 2)

    return distance

def Max_dist(front, right, left, back):
    Max = max(front, right, left, back)
    return Max

def Motor_Way(front, right, left, back):
    if Max == front:
        setMotor(CH1, 50, FORWARD)
        setMotor(CH2, 50, FORWARD)
    elif Max == right:
        setMotor(CH1, 20, FORWARD)
        setMotor(CH2, 50, FORWARD)
    elif Max == left:
        setMotor(CH1, 50, FORWARD)
        setMotor(CH2, 20, FORWARD)
    elif Max == back:
        setMotor(CH1, 50, BACKWARD)
        setMotor(CH2, 50, BACKWARD)

while True:
    frt_dist = dist(frt_trig, frt_echo)
    rig_dist = dist(rig_trig, rig_echo)
    left_dist = dist(left_trig, left_echo)
    back_dist = dist(back_trig, back_echo)
    print("front: {}cm, right: {}cm, left:{}cm, back: {}cm".format(frt_dist,rig_dist,left_dist,back_dist))
    Max = Max_dist(frt_dist, rig_dist, left_dist, back_dist)
    print("Max={}".format(Max))
    Motor = Motor_Way(frt_dist, rig_dist, left_dist, back_dist)