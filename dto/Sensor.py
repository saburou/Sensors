# coding: utf-8

import RPi.GPIO as GPIO
from datetime import datetime

class SensorData:

    def __init__(self, id=None, value=0, timestamp=None):
        self.id = id
        self.value = value
        self.timestamp = timestamp

class Sensor:

    def __init__(self, id, name='unnamed', pinNo=None, available=false, direction=GPIO.IN, mode=GPIO.BOARD):
        '''
            Default pin assignment mode is GPIO.BOARD.
            For example Upper left pin is No.1, Lower right pin is No.40 in Raspberry Pi3.
            If you want to use pin with GPIO No. , set mode to GPIO.BCM.
        '''
        self.id = id
        self.name = name
        self.pinNo = pinNo
        self.available = available
        self.direction = direction
        self.mode = mode

    def read(self):
        '''
            Read input from sensor.
            If function call is invalid, will return None.
        '''
        tmp = None
        if available and GPIO.IN == self.direction:
            GPIO.setmode(self.mode)
            GPIO.setup(self.pinNo, self.direction)
            tmp = SensorData(0,GPIO.input(self.pinNo), datetime.now())
            GPIO.cleanup()

        return tmp

    def write(self, value=0):
        '''
            Output value to sensor.
            If argument value is not integre, will raise InvalidArgumentError.
        '''
        if type(value) is not int:
            raise InvalidArgumentError

        if available and GPIO.OUT == self.direction:
            GPIO.setmode(self.mode)
            GPIO.setup(self.pinNo, self.direction)
            GPIO.output(self.pinNo, value)
            GPIO.cleanup()
