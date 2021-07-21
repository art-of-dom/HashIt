"""
custom_crc_mapping.py
Custom CRC mappings.
"""
from __future__ import absolute_import

import crcmod
from hashit.core.hash_type import HashType

CRCMOD_CUSTOM_MAPPING = {
    HashType.CRC8_CDMA2000: crcmod.mkCrcFun(0x19B,
                                            initCrc=0xFF, rev=False, xorOut=0x00
                                            ),
    HashType.CRC8_DVB_S2: crcmod.mkCrcFun(0x1D5,
                                          initCrc=0x00, rev=False, xorOut=0x00
                                          ),
    HashType.CRC8_EBU: crcmod.mkCrcFun(0x11D,
                                       initCrc=0xFF, rev=True, xorOut=0x00
                                       ),
    HashType.CRC16_A: crcmod.mkCrcFun(0x11021,
                                      initCrc=0x6363, rev=True, xorOut=0x0000
                                      ),
    HashType.CRC16_CMDA2000: crcmod.mkCrcFun(0x1C867,
                                             initCrc=0xFFFF, rev=False, xorOut=0x0000
                                             ),
    HashType.CRC16_DECT_X: crcmod.mkCrcFun(0x10589,
                                           initCrc=0x0000, rev=False, xorOut=0x0000
                                           ),
    HashType.CRC16_TMS37157: crcmod.mkCrcFun(0x11021,
                                             initCrc=0x89EC, rev=True, xorOut=0x0000
                                             ),
}
