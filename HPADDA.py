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


    c_lib = cdll.LoadLibrary('./libhpadda.so')

    def __init__(self):
 #       c_lib = cdll.LoadLibrary('./libhpadda.so')
        res = board.c_lib.initHPADDAboard()
        if res==0:
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
        board.c_lib.ADS1256_SetSampleRate.restype = c_double
        board.c_lib.ADS1256_SetSampleRate.argypes = (c_double, )
        return board.c_lib.ADS1256_SetSampleRate(c_double(rate))


    def delay_us(self, micro_s):
        board.c_lib.delay_us.restype = c_void_p
        board.c_lib.delay_us(c_uint64(micro_s))
        return None

    def get_a_dc(self, ch):
        board.c_lib.ADS1256_GetAdc.restype = c_int32
        return board.c_lib.ADS1256_GetAdc(ch)
