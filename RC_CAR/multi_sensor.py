import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(6, GPIO.OUT) # left trig
GPIO.setup(12, GPIO.IN) #left echo

GPIO.setup(13, GPIO.OUT) # front trig
GPIO.setup(16, GPIO.IN) # front echo

GPIO.setup(26, GPIO.OUT) # right trig
GPIO.setup(19, GPIO.IN) # right echo

print("Start!")

try:
    while True:
        GPIO.output(26, False)
        time.sleep(0.5)

        GPIO.output(26, True)          # 10us 펄스를 내보낸다.
        time.sleep(0.00001)            # Python에서 이 펄스는 실제 100us 근처가 될 것이다
        GPIO.output(26, False)         # 하지만 HC-SR04 센서는 이 오차를 받아준다

        while GPIO.input(19) == 0:     # 18번 핀이 OFF 되는 시점을 시작 시간으로 잡는다
            start = time.time()

        while GPIO.input(19) == 1:     # 18번 핀이 다시 ON 되는 시점을 반사파 수신시간으로 잡는다
            stop = time.time()

        time_interval = stop - start      # 초음파가 수신되는 시간으로 거리를 계산한다
        distance = time_interval * 17000
        distance = round(distance, 2)

        print ("right =>" , distance, "cm")

        GPIO.output(13, False)
        time.sleep(0.5)

        GPIO.output(13, True)          # 10us 펄스를 내보낸다.
        time.sleep(0.00001)            # Python에서 이 펄스는 실제 100us 근처가 될 것이다
        GPIO.output(13, False)         # 하지만 HC-SR04 센서는 이 오차를 받아준다

        while GPIO.input(16) == 0:     # 18번 핀이 OFF 되는 시점을 시작 시간으로 잡는다
            start = time.time()

        while GPIO.input(16) == 1:     # 18번 핀이 다시 ON 되는 시점을 반사파 수신시간으로 잡는다
            stop = time.time()

        time_interval = stop - start      # 초음파가 수신되는 시간으로 거리를 계산한다
        distance = time_interval * 17000
        distance = round(distance, 2)

        print ("front =>" , distance, "cm")

        GPIO.output(6, False)
        time.sleep(0.5)

        GPIO.output(6, True)          # 10us 펄스를 내보낸다.
        time.sleep(0.00001)            # Python에서 이 펄스는 실제 100us 근처가 될 것이다
        GPIO.output(6, False)         # 하지만 HC-SR04 센서는 이 오차를 받아준다

        while GPIO.input(12) == 0:     # 18번 핀이 OFF 되는 시점을 시작 시간으로 잡는다
            start = time.time()

        while GPIO.input(12) == 1:     # 18번 핀이 다시 ON 되는 시점을 반사파 수신시간으로 잡는다
            stop = time.time()

        time_interval = stop - start      # 초음파가 수신되는 시간으로 거리를 계산한다
        distance = time_interval * 17000
        distance = round(distance, 2)

        print ("left =>" , distance, "cm")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Finish")