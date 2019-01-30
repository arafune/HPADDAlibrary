#!/usr/env/bin python3
'''Python module for libhpadda.so

To use this module:
* Run as root
* libhpadda.so is put in the same direcory for this file.
'''

from ctypes import *


class board(object):
    '''
    Wrapper class for HPADDA

    Attributes
    -----------

    '''

    def __init__(self, vref=5.0):
        self.engine = cdll.LoadLibrary('./libhpadda.so')
        self.vref = vref
        res = self.engine.initHPADDAboard()
        if res == 0:
            return None
        else:
            return False

    def readChipId(self):
        id = board.c_lib.ADS1256_ReadChipID()
        if id == 3:
            return True
        else:
            return False

    def setSampleRate(self, rate):
        self.engine.ADS1256_SetSampleRate.restype = c_double
        self.engine.ADS1256_SetSampleRate.argypes = (c_double, )
        return self.engine.ADS1256_SetSampleRate(c_double(rate))

    def delay_us(self, micro_s):
        self.engine.delay_us.restype = c_void_p
        self.engine.delay_us(c_uint64(micro_s))
        return None

    def get_a_dc(self, ch):
        self.engine.ADS1256_GetAdc.restype = c_int32
        return self.engine.ADS1256_GetAdc(ch)

    def get_voltage(self, ch):
        return self.get_a_dc(ch) * self.vref / 0x7fffff

    def close(self):
        self.engine.closeHPADDAboard()
        return None
