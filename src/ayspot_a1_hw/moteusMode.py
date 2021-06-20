import argparse
import enum
import io
import math
import serial
import struct

class MoteusMode(enum.IntEnum):
    STOPPED = 0
    FAULT = 1
    PWM = 5
    VOLTAGE = 6
    VOLTAGE_FOC = 7
    VOLTAGE_DQ = 8
    CURRENT = 9
    POSITION = 10
    TIMEOUT = 11
    ZERO_VEL = 12

