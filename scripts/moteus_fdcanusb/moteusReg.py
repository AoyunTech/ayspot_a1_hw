import argparse
import enum
import io
import math
import serial
import struct

class MoteusReg():
    # These constants can be found in:
    # https://github.com/mjbots/moteus/blob/master/docs/reference.md under
    # "register command set".
    INT8 = 0
    INT16 = 1
    INT32 = 2
    F32 = 3

    WRITE_BASE = 0x00
    READ_BASE = 0x10
    REPLY_BASE = 0x20
    WRITE_ERROR = 0x30
    READ_ERROR = 0x31
    NOP = 0x50

    _TYPE_STRUCTS = {
        INT8: struct.Struct('<b'),
        INT16: struct.Struct('<h'),
        INT32: struct.Struct('<i'),
        F32: struct.Struct('<f'),
    }

    MOTEUS_REG_MODE = 0x000
    MOTEUS_REG_POSITION = 0x001
    MOTEUS_REG_VELOCITY = 0x002
    MOTEUS_REG_TORQUE = 0x003
    MOTEUS_REG_Q_A = 0x004
    MOTEUS_REG_D_A = 0x005
    MOTEUS_REG_V = 0x00d
    MOTEUS_REG_TEMP_C = 0x00e
    MOTEUS_REG_FAULT = 0x00f

    MOTEUS_REG_POS_POSITION = 0x20
    MOTEUS_REG_POS_VELOCITY = 0x21
    MOTEUS_REG_POS_TORQUE = 0x22
    MOTEUS_REG_POS_KP = 0x23
    MOTEUS_REG_POS_KD = 0x24
    MOTEUS_REG_MAX_TORQUE = 0x25
