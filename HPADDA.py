#!/usr/env/bin python3
'''Python module for libhpadda.so

To use this module:
* Run as root
* libhpadda.so is put in the same direcory for this file.
'''

import ctypes


class Board():
    '''
    Wrapper class for HPADDA

    Attributes
    -----------

    '''

    def __init__(self, vref=5.0):
        '''Init ADS1256

        Parameters
        ----------
        vref: float
           Vref. (default=5.0)

        Return
        -------
        None
'''
        self.engine = ctypes.cdll.LoadLibrary('./libhpadda.so')
        self.vref = vref
        self.engine.initHPADDAboard()

    def read_chip_id(self):
        ''''Return Chip ID (Default3)
'''
        id_num = self.engine.ADS1256_ReadChipID()
        if id_num == 3:
            return True
        return False

    def set_sample_rate(self, rate):
        '''Set sample rate

        Return
        -------
        float

'''
        self.engine.ADS1256_SetSampleRate.restype = ctypes.c_double
        self.engine.ADS1256_SetSampleRate.argypes = (ctypes.c_double, )
        return self.engine.ADS1256_SetSampleRate(ctypes.c_double(rate))

    def delay_us(self, micro_s):
        '''Wait microseconds

        Parameters
        ----------
        micro_s: int
'''
        self.engine.delay_us.restype = ctypes.c_void_p
        self.engine.delay_us(ctypes.c_uint64(micro_s))

    def get_adc(self, ch_0_7):
        '''Get quantized voltage

        Parameters
        ----------
        ch: int
            channel number (0-7)

        Return
        -------
        ADC: int
        '''
        self.engine.ADS1256_GetAdc.restype = ctypes.c_int32
        return self.engine.ADS1256_GetAdc(ch_0_7)

    def get_voltage(self, ch_0_7):
        '''
        Parameters
        ----------
        ch: int
            channel number (0-7)

        Return
        -------
        Voltage: float
'''
        return self.get_adc(ch_0_7) * self.vref / 0x7fffff

    def close(self):
        '''close ADS1256
        '''
        self.engine.closeHPADDAboard()
