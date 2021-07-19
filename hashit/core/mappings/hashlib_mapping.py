"""
hashlib_mapping.py
Mapping hash lib syle functions to hash types.
"""
from __future__ import absolute_import

import hashlib

import crcmod

from hashit.core.hash_type import HashType


HASHLIB_MAPPING = {
    HashType.CRC8: crcmod.predefined.Crc('crc-8').new,
    HashType.CRC8_DARC: crcmod.predefined.Crc('crc-8-darc').new,
    HashType.CRC8_I_CODE: crcmod.predefined.Crc('crc-8-i-code').new,
    HashType.CRC8_ITU: crcmod.predefined.Crc('crc-8-itu').new,
    HashType.CRC8_MAXIM: crcmod.predefined.Crc('crc-8-maxim').new,
    HashType.CRC8_ROHC: crcmod.predefined.Crc('crc-8-rohc').new,
    HashType.CRC8_WCDMA: crcmod.predefined.Crc('crc-8-wcdma').new,
    HashType.CRC16: crcmod.predefined.Crc('crc-16').new,
    HashType.CRC16_AUG_CCITT: crcmod.predefined.Crc('crc-aug-ccitt').new,
    HashType.CRC16_BUYPASS: crcmod.predefined.Crc('crc-16-buypass').new,
    HashType.CRC16_CCITT_FALSE: crcmod.predefined.Crc('crc-ccitt-false').new,
    HashType.CRC16_DDS_110: crcmod.predefined.Crc('crc-16-dds-110').new,
    HashType.CRC16_DECT_R: crcmod.predefined.Crc('crc-16-dect').new,
    HashType.CRC16_DNP: crcmod.predefined.Crc('crc-16-dnp').new,
    HashType.CRC16_EN_13757: crcmod.predefined.Crc('crc-16-en-13757').new,
    HashType.CRC16_GENIUS: crcmod.predefined.Crc('crc-16-genibus').new,
    HashType.CRC16_KERMIT: crcmod.predefined.Crc('kermit').new,
    HashType.CRC16_MAXIM: crcmod.predefined.Crc('crc-16-maxim').new,
    HashType.CRC16_MCRF4XX: crcmod.predefined.Crc('crc-16-mcrf4xx').new,
    HashType.CRC16_MODBUS: crcmod.predefined.Crc('modbus').new,
    HashType.CRC16_RIELLO: crcmod.predefined.Crc('crc-16-riello').new,
    HashType.CRC16_T10_DIF: crcmod.predefined.Crc('crc-16-t10-dif').new,
    HashType.CRC16_TELEDISK: crcmod.predefined.Crc('crc-16-teledisk').new,
    HashType.CRC16_USB: crcmod.predefined.Crc('crc-16-usb').new,
    HashType.CRC16_X_25: crcmod.predefined.Crc('x-25').new,
    HashType.CRC16_XMODEM: crcmod.predefined.Crc('xmodem').new,
    HashType.CRC32: crcmod.predefined.Crc('crc-32').new,
    HashType.CRC64: crcmod.predefined.Crc('crc-64').new,
    HashType.MD5: hashlib.md5,
    HashType.SHA1: hashlib.sha1,
    HashType.SHA224: hashlib.sha224,
    HashType.SHA256: hashlib.sha256,
    HashType.SHA384: hashlib.sha384,
    HashType.SHA512: hashlib.sha512
}
