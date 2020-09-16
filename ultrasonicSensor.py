import RPi.GPIO as gpio
import time

print("starr")

frt_trig = 20
frt_echo = 21

rig_trig = 13
rig_echo = 16

left_trig = 6
left_echo = 12

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

gpio.setup(frt_trig , gpio.OUT)
gpio.setup(rig_trig , gpio.OUT)
gpio.setup(left_trig , gpio.OUT)

gpio.setup(frt_echo , gpio.IN)
gpio.setup(rig_echo , gpio.IN)
gpio.setup(left_echo , gpio.IN)

def dist(trig, echo):
    global  str, end
    gpio.output(trig, False)
    time.sleep(0.5)
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    while gpio.input(echo) == 0:
        srt = time.time()
    while gpio.input(echo) == 1:
        end = time.time()

    puls_drtn = end-srt
    distance = puls_drtn * 17000
    distance = round(distance, 2)

while True:
    frt_dist = dist(frt_trig, frt_echo)
    rig_dist = dist(rig_trig, rig_echo)
    left_dist = dist(left_trig, left_echo)
    print("frt_dist: {}cm/ rig_dist: {}cm/ left_dist: {}cm".format(frt_dist,rig_dist,left_dist))
