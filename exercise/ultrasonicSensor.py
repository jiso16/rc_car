import RPi.GPIO as GPIO
import time

frt_trig = 26
frt_echo = 19

rig_trig = 13
rig_echo = 16

left_trig = 6
left_echo = 12

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(frt_trig , GPIO.OUT)
GPIO.setup(rig_trig , GPIO.OUT)
GPIO.setup(left_trig , GPIO.OUT)

GPIO.setup(frt_echo , GPIO.IN)
GPIO.setup(rig_echo , GPIO.IN)
GPIO.setup(left_echo , GPIO.IN)

def dist(name_list, trig, echo):
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

    print(name_list,"dist: ",distance)

while True:
    frt_dist = dist("front",frt_trig, frt_echo)
    rig_dist = dist("right",rig_trig, rig_echo)
    left_dist = dist("left", left_trig, left_echo)