import RPi.GPIO as GPIO
import time

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
        print("front")
    elif Max == right:
        print("right")
    elif Max == left:
        print("left")
    elif Max == back:
        print("back")

while True:
    frt_dist = dist(frt_trig, frt_echo)
    rig_dist = dist(rig_trig, rig_echo)
    left_dist = dist(left_trig, left_echo)
    back_dist = dist(back_trig, back_echo)
    print("front: {}cm, right: {}cm, left:{}cm, back: {}cm".format(frt_dist,rig_dist,left_dist,back_dist))
    Max = Max_dist(frt_dist, rig_dist, left_dist, back_dist)
    print("Max={}".format(Max))
    Motor = Motor_Way(frt_dist, rig_dist, left_dist, back_dist)