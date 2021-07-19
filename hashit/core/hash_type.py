"""
HashType.py

Enumerates the hash types to easily allow choosing a hash.
"""

from enum import Enum


class HashType(Enum):
    """An Enumerated representation of a hash used for parsing"""

    CRC8 = 0
    CRC8_CDMA2000 = 1
    CRC8_DARC = 2
    CRC8_DVB_S2 = 3
    CRC8_EBU = 4
    CRC8_I_CODE = 5
    CRC8_ITU = 6
    CRC8_MAXIM = 7
    CRC8_ROHC = 8
    CRC8_WCDMA = 9
    CRC16 = 10
    CRC16_A = 11
    CRC16_AUG_CCITT = 12
    CRC16_BUYPASS = 13
    CRC16_CMDA2000 = 14
    CRC16_CCITT_FALSE = 15
    CRC16_DDS_110 = 16
    CRC16_DECT_R = 17
    CRC16_DECT_X = 18
    CRC16_DNP = 19
    CRC16_EN_13757 = 20
    CRC16_GENIUS = 21
    CRC16_KERMIT = 22
    CRC16_MAXIM = 23
    CRC16_MCRF4XX = 24
    CRC16_MODBUS = 25
    CRC16_RIELLO = 26
    CRC16_T10_DIF = 27
    CRC16_TELEDISK = 28
    CRC16_TMS37157 = 29
    CRC16_USB = 30
    CRC16_X_25 = 31
    CRC16_XMODEM = 32
    CRC32 = 33
    CRC64 = 34
    MD2 = 35
    MD4 = 36
    MD5 = 37
    SHA1 = 38
    SHA224 = 39
    SHA256 = 40
    SHA384 = 41
    SHA512 = 42

    def is_crc(self):
        "Checks if hash is a crc"
        return self.name.startswith('CRC')

    def is_md(self):
        "Checks if hash is an md hash"
        return self.name.startswith('MD')

    def is_sha(self):
        "Checks if hash is an sha hash"
        return self.name.startswith('SHA')

    def hash_byte_length(self):
        """Gives the length in bytes of the hash"""
        if self.is_crc():
            return self._crc_byte_len()
        if self.is_md():
            return 16
        if self.is_sha():
            return self._sha_byte_len()
        return 0

    def hash_str_length(self):
        """Gives the length in characters of the hash"""
        return self.hash_byte_length() * 2

    def _crc_byte_len(self):
        if self in CRC8_LIST:
            return 1
        if self in CRC16_LIST:
            return 2
        if self is HashType.CRC32:
            return 4
        if self is HashType.CRC64:
            return 8
        return 0

    def _sha_byte_len(self):
        if self is HashType.SHA1:
            return 20
        if self is HashType.SHA224:
            return 28
        if self is HashType.SHA256:
            return 32
        if self is HashType.SHA384:
            return 48
        if self is HashType.SHA512:
            return 64
        return 0


CRC8_LIST = [
    HashType.CRC8,
    HashType.CRC8_CDMA2000,
    HashType.CRC8_DARC,
    HashType.CRC8_DVB_S2,
    HashType.CRC8_EBU,
    HashType.CRC8_I_CODE,
    HashType.CRC8_ITU,
    HashType.CRC8_MAXIM,
    HashType.CRC8_ROHC,
    HashType.CRC8_WCDMA
]


CRC16_LIST = [
    HashType.CRC16,
    HashType.CRC16_A,
    HashType.CRC16_AUG_CCITT,
    HashType.CRC16_BUYPASS,
    HashType.CRC16_CMDA2000,
    HashType.CRC16_CCITT_FALSE,
    HashType.CRC16_DDS_110,
    HashType.CRC16_DECT_R,
    HashType.CRC16_DECT_X,
    HashType.CRC16_DNP,
    HashType.CRC16_EN_13757,
    HashType.CRC16_GENIUS,
    HashType.CRC16_KERMIT,
    HashType.CRC16_MAXIM,
    HashType.CRC16_MCRF4XX,
    HashType.CRC16_MODBUS,
    HashType.CRC16_RIELLO,
    HashType.CRC16_T10_DIF,
    HashType.CRC16_TELEDISK,
    HashType.CRC16_TMS37157,
    HashType.CRC16_USB,
    HashType.CRC16_X_25,
    HashType.CRC16_XMODEM
]

MD_LIST = [
    HashType.MD2,
    HashType.MD4,
    HashType.MD5,
]
