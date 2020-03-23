import serial
from serial import Serial


def test_device():
    try:
        ser = serial.Serial('COM3', 9600)
    except:
        return False
    return True


def use_device():
    try:
        ser = serial.Serial('COM3', 9600)
    except:
        return False
    f = open('./media/out.csv', 'w')
    while True:
        line = ser.readline().decode('utf-8')[:-1]
        if "EOF" in line:
            break
        f.write(line)
        print(line)
    f.close()
    ser.close()
