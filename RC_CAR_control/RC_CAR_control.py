import RPi.GPIO as GPIO
import time
import serial

STOP = 0
FORWARD = 1
BACKWORD = 2

CH1 = 0
CH2 = 1

OUTPUT = 1
INPUT = 0

HIGH = 1
LOW = 0

ENA = 26  # board 37 pin
ENB = 0  # board 27 pin

IN1 = 19  # board 35 pin
IN2 = 13  # board 33 pin
IN3 = 6  # board 31 pin
IN4 = 5  # board 29 pin

SERIALPORT = "/dev/serial0"
# SERIALPORT = "/dev/ttyUSB0"
# SERIALPORT = "/dev/ttyAMA0"

# set uart
BAUDRATE = 115200
ser = serial.Serial(SERIALPORT, BAUDRATE)
ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = None
ser.xonxoff = False
ser.rtscts = False
ser.dsrdtr = False
ser.writeTimeout = 0
print ("Starting Up Serial Monitor")


# RC Code

def setPinConfig(EN, INA, INB):
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    pwm = GPIO.PWM(EN, 100)
    pwm.start(0)
    return pwm


def setMotorContorl(pwm, INA, INB, speed, stat):
    pwm.ChangeDutyCycle(speed)
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
    elif stat == BACKWORD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)


def setMotor(ch, speed, stat):
    if ch == CH1:
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        setMotorContorl(pwmB, IN3, IN4, speed, stat)


# Below Server code

GPIO.setmode(GPIO.BCM)  # programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
GPIO.setwarnings(False)

pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

try:
    ser.open()
except Exception as e:
    print ("Exception: Opening serial port: " + str(e))
# finally:
# ser.close()
if ser.isOpen():
    while 1:
        ser.flushOutput()
        ser_bytes = ser.readline()
        decoded_bytes = (ser_bytes.decode("utf-8"))
        print('Receiving')
        print('Rx Data: ' + decoded_bytes)
        # print(type(decoded_bytes))
        # print(len(decoded_bytes))
        if decoded_bytes[0] == '1':
            setMotor(CH1, 50, FORWARD)
            setMotor(CH2, 50, FORWARD)
        elif decoded_bytes[0] == '0':
            setMotor(CH1, 50, BACKWORD)
            setMotor(CH2, 50, BACKWORD)
        elif decoded_bytes[0] == 'l':
            setMotor(CH1, 70, FORWARD)
            setMotor(CH2, 0, FORWARD)
        elif decoded_bytes[0] == 'r':
            setMotor(CH1, 0, FORWARD)
            setMotor(CH2, 80, FORWARD)
        elif decoded_bytes[0] == 'q':
            setMotor(CH1, 80, STOP)
            setMotor(CH2, 80, STOP)
        # elif decoded_bytes[0] == 'e':
        # setMotor(CH1, 80, STOP)
        # setMotor(CH2, 80, STOP)
        # break
    time.sleep(0.5)
# programming..
else:
    print ("Cannot open serial port.")


