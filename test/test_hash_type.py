'''Tests for the HashType Enum'''

from __future__ import absolute_import
import unittest
from nose.tools import assert_equals, assert_true, assert_false
from hashit.core.hash_type import HashType

# pylint: disable=missing-docstring
# pylint: disable=invalid-name
# pylint: disable=no-self-use
# pylint: disable=too-many-public-methods


class TestHashType(unittest.TestCase):

    # CRC 8
    def test_hash_type_crc8_in_hash_type(self):
        assert_true('CRC8' in HashType.__members__)

    def test_hash_type_crc8_lookup(self):
        assert_equals(HashType.CRC8, HashType['CRC8'])

    def test_hash_type_crc8_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8.hash_byte_length())

    def test_hash_type_crc8_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8.hash_str_length())

    def test_hash_type_crc8_is_crc(self):
        assert_true(HashType.CRC8.is_crc())

    def test_hash_type_crc8_is_not_md(self):
        assert_false(HashType.CRC8.is_md())

    def test_hash_type_crc8_is_not_sha(self):
        assert_false(HashType.CRC8.is_sha())

    def test_hash_type_crc8_cdma2000_in_hash_type(self):
        assert_true('CRC8_CDMA2000' in HashType.__members__)

    def test_hash_type_crc8_cdma2000_lookup(self):
        assert_equals(HashType.CRC8_CDMA2000, HashType['CRC8_CDMA2000'])

    def test_hash_type_crc8_cdma2000_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_CDMA2000.hash_byte_length())

    def test_hash_type_crc8_cdma2000_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_CDMA2000.hash_str_length())

    def test_hash_type_crc8_cdma2000_is_crc(self):
        assert_true(HashType.CRC8_CDMA2000.is_crc())

    def test_hash_type_crc8_cdma2000_is_not_md(self):
        assert_false(HashType.CRC8_CDMA2000.is_md())

    def test_hash_type_crc8_cdma2000_is_not_sha(self):
        assert_false(HashType.CRC8_CDMA2000.is_sha())

    def test_hash_type_crc8_darc_in_hash_type(self):
        assert_true('CRC8_DARC' in HashType.__members__)

    def test_hash_type_crc8_darc_lookup(self):
        assert_equals(HashType.CRC8_DARC, HashType['CRC8_DARC'])

    def test_hash_type_crc8_darc_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_DARC.hash_byte_length())

    def test_hash_type_crc8_darc_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_DARC.hash_str_length())

    def test_hash_type_crc8_darc_is_crc(self):
        assert_true(HashType.CRC8_DARC.is_crc())

    def test_hash_type_crc8_darc_is_not_md(self):
        assert_false(HashType.CRC8_DARC.is_md())

    def test_hash_type_crc8_darc_is_not_sha(self):
        assert_false(HashType.CRC8_DARC.is_sha())

    def test_hash_type_crc8_dvb_s2_in_hash_type(self):
        assert_true('CRC8_DVB_S2' in HashType.__members__)

    def test_hash_type_crc8_dvb_s2_lookup(self):
        assert_equals(HashType.CRC8_DVB_S2, HashType['CRC8_DVB_S2'])

    def test_hash_type_crc8_dvb_s2_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_DVB_S2.hash_byte_length())

    def test_hash_type_crc8_dvb_s2_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_DVB_S2.hash_str_length())

    def test_hash_type_crc8_dvb_s2_is_crc(self):
        assert_true(HashType.CRC8_DVB_S2.is_crc())

    def test_hash_type_crc8_dvb_s2_is_not_md(self):
        assert_false(HashType.CRC8_DVB_S2.is_md())

    def test_hash_type_crc8_dvb_s2_is_not_sha(self):
        assert_false(HashType.CRC8_DVB_S2.is_sha())

    def test_hash_type_crc8_ebu_in_hash_type(self):
        assert_true('CRC8_EBU' in HashType.__members__)

    def test_hash_type_crc8_ebu_lookup(self):
        assert_equals(HashType.CRC8_EBU, HashType['CRC8_EBU'])

    def test_hash_type_crc8_ebu_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_EBU.hash_byte_length())

    def test_hash_type_crc8_ebu_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_EBU.hash_str_length())

    def test_hash_type_crc8_ebu_is_crc(self):
        assert_true(HashType.CRC8_EBU.is_crc())

    def test_hash_type_crc8_ebu_is_not_md(self):
        assert_false(HashType.CRC8_EBU.is_md())

    def test_hash_type_crc8_ebu_is_not_sha(self):
        assert_false(HashType.CRC8_EBU.is_sha())

    def test_hash_type_crc8_i_code_in_hash_type(self):
        assert_true('CRC8_I_CODE' in HashType.__members__)

    def test_hash_type_crc8_i_code_lookup(self):
        assert_equals(HashType.CRC8_I_CODE, HashType['CRC8_I_CODE'])

    def test_hash_type_crc8_i_code_has_hash_str_length_1(self):
        assert_equals(1, HashType.CRC8_I_CODE.hash_byte_length())

    def test_hash_type_crc8_i_code_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_I_CODE.hash_str_length())

    def test_hash_type_crc8_i_code_is_crc(self):
        assert_true(HashType.CRC8_I_CODE.is_crc())

    def test_hash_type_crc8_i_code_is_not_md(self):
        assert_false(HashType.CRC8_I_CODE.is_md())

    def test_hash_type_crc8_i_code_is_not_sha(self):
        assert_false(HashType.CRC8_I_CODE.is_sha())

    def test_hash_type_crc8_itu_in_hash_type(self):
        assert_true('CRC8_ITU' in HashType.__members__)

    def test_hash_type_crc8_itu_lookup(self):
        assert_equals(HashType.CRC8_ITU, HashType['CRC8_ITU'])

    def test_hash_type_crc8_itu_has_hash_str_length_1(self):
        assert_equals(1, HashType.CRC8_ITU.hash_byte_length())

    def test_hash_type_crc8_itu_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_ITU.hash_str_length())

    def test_hash_type_crc8_itu_is_crc(self):
        assert_true(HashType.CRC8_ITU.is_crc())

    def test_hash_type_crc8_itu_is_not_md(self):
        assert_false(HashType.CRC8_ITU.is_md())

    def test_hash_type_crc8_itu_is_not_sha(self):
        assert_false(HashType.CRC8_ITU.is_sha())

    def test_hash_type_crc8_maxim_in_hash_type(self):
        assert_true('CRC8_MAXIM' in HashType.__members__)

    def test_hash_type_crc8_maxim_lookup(self):
        assert_equals(HashType.CRC8_MAXIM, HashType['CRC8_MAXIM'])

    def test_hash_type_crc8_maxim_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_MAXIM.hash_byte_length())

    def test_hash_type_crc8_maxim_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_MAXIM.hash_str_length())

    def test_hash_type_crc8_MAXIM_is_crc(self):
        assert_true(HashType.CRC8_MAXIM.is_crc())

    def test_hash_type_crc8_maxim_is_not_md(self):
        assert_false(HashType.CRC8_MAXIM.is_md())

    def test_hash_type_crc8_maxim_is_not_sha(self):
        assert_false(HashType.CRC8_MAXIM.is_sha())

    def test_hash_type_crc8_rohc_in_hash_type(self):
        assert_true('CRC8_ROHC' in HashType.__members__)

    def test_hash_type_crc8_rohc_lookup(self):
        assert_equals(HashType.CRC8_ROHC, HashType['CRC8_ROHC'])

    def test_hash_type_crc8_rohc_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_ROHC.hash_byte_length())

    def test_hash_type_crc8_rohc_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_ROHC.hash_str_length())

    def test_hash_type_crc8_rohc_is_crc(self):
        assert_true(HashType.CRC8_ROHC.is_crc())

    def test_hash_type_crc8_rohc_is_not_md(self):
        assert_false(HashType.CRC8_ROHC.is_md())

    def test_hash_type_crc8_rohc_is_not_sha(self):
        assert_false(HashType.CRC8_ROHC.is_sha())

    def test_hash_type_crc8_wcdma_in_hash_type(self):
        assert_true('CRC8_WCDMA' in HashType.__members__)

    def test_hash_type_crc8_wcdma_lookup(self):
        assert_equals(HashType.CRC8_WCDMA, HashType['CRC8_WCDMA'])

    def test_hash_type_crc8_wcdma_has_hash_byte_length_1(self):
        assert_equals(1, HashType.CRC8_WCDMA.hash_byte_length())

    def test_hash_type_crc8_wcdma_has_hash_str_length_2(self):
        assert_equals(2, HashType.CRC8_WCDMA.hash_str_length())

    def test_hash_type_crc8_wcdma_is_crc(self):
        assert_true(HashType.CRC8_WCDMA.is_crc())

    def test_hash_type_crc8_wcdma_is_not_md(self):
        assert_false(HashType.CRC8_WCDMA.is_md())

    def test_hash_type_crc8_wcdma_is_not_sha(self):
        assert_false(HashType.CRC8_WCDMA.is_sha())

    # CRC16

    def test_hash_type_crc16_in_hash_type(self):
        assert_true('CRC16' in HashType.__members__)

    def test_hash_type_crc16_lookup(self):
        assert_equals(HashType.CRC16, HashType['CRC16'])

    def test_hash_type_crc16_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16.hash_byte_length())

    def test_hash_type_crc16_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16.hash_str_length())

    def test_hash_type_crc16_a_in_hash_type(self):
        assert_true('CRC16_A' in HashType.__members__)

    def test_hash_type_crc16_a_lookup(self):
        assert_equals(HashType.CRC16_A, HashType['CRC16_A'])

    def test_hash_type_crc16_a_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_A.hash_byte_length())

    def test_hash_type_crc16_a_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_A.hash_str_length())

    def test_hash_type_crc16_aug_ccitt_in_hash_type(self):
        assert_true('CRC16_AUG_CCITT' in HashType.__members__)

    def test_hash_type_crc16_aug_ccitt_lookup(self):
        assert_equals(HashType.CRC16_AUG_CCITT, HashType['CRC16_AUG_CCITT'])

    def test_hash_type_crc16_aug_ccitt_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_AUG_CCITT.hash_byte_length())

    def test_hash_type_crc16_aug_ccitt_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_AUG_CCITT.hash_str_length())

    def test_hash_type_crc16_buypass_in_hash_type(self):
        assert_true('CRC16_BUYPASS' in HashType.__members__)

    def test_hash_type_crc16_buypass_lookup(self):
        assert_equals(HashType.CRC16_BUYPASS, HashType['CRC16_BUYPASS'])

    def test_hash_type_crc16_buypass_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_BUYPASS.hash_byte_length())

    def test_hash_type_crc16_buypass_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_BUYPASS.hash_str_length())

    def test_hash_type_crc16_cmda2000_in_hash_type(self):
        assert_true('CRC16_CMDA2000' in HashType.__members__)

    def test_hash_type_crc16_cmda2000_lookup(self):
        assert_equals(HashType.CRC16_CMDA2000, HashType['CRC16_CMDA2000'])

    def test_hash_type_crc16_cmda2000_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_CMDA2000.hash_byte_length())

    def test_hash_type_crc16_cmda2000_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_CMDA2000.hash_str_length())

    def test_hash_type_crc16_ccitt_false_in_hash_type(self):
        assert_true('CRC16_CCITT_FALSE' in HashType.__members__)

    def test_hash_type_crc16_ccitt_false_lookup(self):
        assert_equals(HashType.CRC16_CCITT_FALSE, HashType['CRC16_CCITT_FALSE'])

    def test_hash_type_crc16_ccitt_false_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_CCITT_FALSE.hash_byte_length())

    def test_hash_type_crc16_ccitt_false_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_CCITT_FALSE.hash_str_length())

    def test_hash_type_crc16_dds_110_in_hash_type(self):
        assert_true('CRC16_DDS_110' in HashType.__members__)

    def test_hash_type_crc16_dds_110_lookup(self):
        assert_equals(HashType.CRC16_DDS_110, HashType['CRC16_DDS_110'])

    def test_hash_type_crc16_dds_110_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DDS_110.hash_byte_length())

    def test_hash_type_crc16_dds_110_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DDS_110.hash_str_length())

    def test_hash_type_crc16_dect_r_in_hash_type(self):
        assert_true('CRC16_DECT_R' in HashType.__members__)

    def test_hash_type_crc16_dect_r_lookup(self):
        assert_equals(HashType.CRC16_DECT_R, HashType['CRC16_DECT_R'])

    def test_hash_type_crc16_dect_r_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DECT_R.hash_byte_length())

    def test_hash_type_crc16_dect_r_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DECT_R.hash_str_length())

    def test_hash_type_crc16_dect_x_in_hash_type(self):
        assert_true('CRC16_DECT_X' in HashType.__members__)

    def test_hash_type_crc16_dect_x_lookup(self):
        assert_equals(HashType.CRC16_DECT_X, HashType['CRC16_DECT_X'])

    def test_hash_type_crc16_dect_x_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DECT_X.hash_byte_length())

    def test_hash_type_crc16_dect_x_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DECT_X.hash_str_length())

    def test_hash_type_crc16_dnp_in_hash_type(self):
        assert_true('CRC16_DNP' in HashType.__members__)

    def test_hash_type_crc16_dnp_lookup(self):
        assert_equals(HashType.CRC16_DNP, HashType['CRC16_DNP'])

    def test_hash_type_crc16_dnp_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_DNP.hash_byte_length())

    def test_hash_type_crc16_dnp_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_DNP.hash_str_length())

    def test_hash_type_crc16_en_13757_in_hash_type(self):
        assert_true('CRC16_EN_13757' in HashType.__members__)

    def test_hash_type_crc16_en_13757_lookup(self):
        assert_equals(HashType.CRC16_EN_13757, HashType['CRC16_EN_13757'])

    def test_hash_type_crc16_en_13757_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_EN_13757.hash_byte_length())

    def test_hash_type_crc16_en_13757_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_EN_13757.hash_str_length())

    def test_hash_type_crc16_genius_in_hash_type(self):
        assert_true('CRC16_GENIUS' in HashType.__members__)

    def test_hash_type_crc16_genius_lookup(self):
        assert_equals(HashType.CRC16_GENIUS, HashType['CRC16_GENIUS'])

    def test_hash_type_crc16_genius_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_GENIUS.hash_byte_length())

    def test_hash_type_crc16_genius_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_GENIUS.hash_str_length())

    def test_hash_type_crc16_kermit_in_hash_type(self):
        assert_true('CRC16_KERMIT' in HashType.__members__)

    def test_hash_type_crc16_kermit_lookup(self):
        assert_equals(HashType.CRC16_KERMIT, HashType['CRC16_KERMIT'])

    def test_hash_type_crc16_kermit_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_KERMIT.hash_byte_length())

    def test_hash_type_crc16_kermit_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_KERMIT.hash_str_length())

    def test_hash_type_crc16_maxim_in_hash_type(self):
        assert_true('CRC16_MAXIM' in HashType.__members__)

    def test_hash_type_crc16_maxim_lookup(self):
        assert_equals(HashType.CRC16_MAXIM, HashType['CRC16_MAXIM'])

    def test_hash_type_crc16_maxim_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MAXIM.hash_byte_length())

    def test_hash_type_crc16_maxim_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MAXIM.hash_str_length())

    def test_hash_type_crc16_mcrf4xx_in_hash_type(self):
        assert_true('CRC16_MCRF4XX' in HashType.__members__)

    def test_hash_type_crc16_mcrf4xx_lookup(self):
        assert_equals(HashType.CRC16_MCRF4XX, HashType['CRC16_MCRF4XX'])

    def test_hash_type_crc16_mcrf4xx_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MCRF4XX.hash_byte_length())

    def test_hash_type_crc16_mcrf4xx_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MCRF4XX.hash_str_length())

    def test_hash_type_crc16_modbus_in_hash_type(self):
        assert_true('CRC16_MODBUS' in HashType.__members__)

    def test_hash_type_crc16_modbus_lookup(self):
        assert_equals(HashType.CRC16_MODBUS, HashType['CRC16_MODBUS'])

    def test_hash_type_crc16_modbus_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_MODBUS.hash_byte_length())

    def test_hash_type_crc16_modbus_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_MODBUS.hash_str_length())

    def test_hash_type_crc16_riello_in_hash_type(self):
        assert_true('CRC16_RIELLO' in HashType.__members__)

    def test_hash_type_crc16_riello_lookup(self):
        assert_equals(HashType.CRC16_RIELLO, HashType['CRC16_RIELLO'])

    def test_hash_type_crc16_riello_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_RIELLO.hash_byte_length())

    def test_hash_type_crc16_riello_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_RIELLO.hash_str_length())

    def test_hash_type_crc16_t10_dif_in_hash_type(self):
        assert_true('CRC16_T10_DIF' in HashType.__members__)

    def test_hash_type_crc16_t10_dif_lookup(self):
        assert_equals(HashType.CRC16_T10_DIF, HashType['CRC16_T10_DIF'])

    def test_hash_type_crc16_t10_dif_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_T10_DIF.hash_byte_length())

    def test_hash_type_crc16_t10_dif_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_T10_DIF.hash_str_length())

    def test_hash_type_crc16_teledisk_in_hash_type(self):
        assert_true('CRC16_TELEDISK' in HashType.__members__)

    def test_hash_type_crc16_teledisk_lookup(self):
        assert_equals(HashType.CRC16_TELEDISK, HashType['CRC16_TELEDISK'])

    def test_hash_type_crc16_teledisk_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_TELEDISK.hash_byte_length())

    def test_hash_type_crc16_teledisk_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_TELEDISK.hash_str_length())

    def test_hash_type_crc16_tms37157_in_hash_type(self):
        assert_true('CRC16_TMS37157' in HashType.__members__)

    def test_hash_type_crc16_tms37157_lookup(self):
        assert_equals(HashType.CRC16_TMS37157, HashType['CRC16_TMS37157'])

    def test_hash_type_crc16_tms37157_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_TMS37157.hash_byte_length())

    def test_hash_type_crc16_tms37157_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_TMS37157.hash_str_length())

    def test_hash_type_crc16_usb_in_hash_type(self):
        assert_true('CRC16_USB' in HashType.__members__)

    def test_hash_type_crc16_usb_lookup(self):
        assert_equals(HashType.CRC16_USB, HashType['CRC16_USB'])

    def test_hash_type_crc16_usb_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_USB.hash_byte_length())

    def test_hash_type_crc16_usb_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_USB.hash_str_length())

    def test_hash_type_crc16_x_25_in_hash_type(self):
        assert_true('CRC16_X_25' in HashType.__members__)

    def test_hash_type_crc16_x_25_usb_lookup(self):
        assert_equals(HashType.CRC16_X_25, HashType['CRC16_X_25'])

    def test_hash_type_crc16_x_25_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_X_25.hash_byte_length())

    def test_hash_type_crc16_x_25_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_X_25.hash_str_length())

    def test_hash_type_crc16_xmodem_in_hash_type(self):
        assert_true('CRC16_XMODEM' in HashType.__members__)

    def test_hash_type_crc16_xmodem_lookup(self):
        assert_equals(HashType.CRC16_XMODEM, HashType['CRC16_XMODEM'])

    def test_hash_type_crc16_xmodem_has_hash_byte_length_2(self):
        assert_equals(2, HashType.CRC16_XMODEM.hash_byte_length())

    def test_hash_type_crc16_xmodem_has_hash_str_length_4(self):
        assert_equals(4, HashType.CRC16_XMODEM.hash_str_length())

    # Others

    def test_hash_type_crc32_in_hash_type(self):
        assert_true('CRC32' in HashType.__members__)

    def test_hash_type_crc32_lookup(self):
        assert_equals(HashType.CRC32, HashType['CRC32'])

    def test_hash_type_crc32_has_hash_byte_length_4(self):
        assert_equals(4, HashType.CRC32.hash_byte_length())

    def test_hash_type_crc32_has_hash_str_length_8(self):
        assert_equals(8, HashType.CRC32.hash_str_length())

    def test_hash_type_crc64_in_hash_type(self):
        assert_true('CRC64' in HashType.__members__)

    def test_hash_type_crc64_lookup(self):
        assert_equals(HashType.CRC64, HashType['CRC64'])

    def test_hash_type_crc64_has_hash_byte_length_8(self):
        assert_equals(8, HashType.CRC64.hash_byte_length())

    def test_hash_type_crc64_has_hash_str_length_16(self):
        assert_equals(16, HashType.CRC64.hash_str_length())

    def test_hash_type_md2_in_hash_type(self):
        assert_true('MD2' in HashType.__members__)

    def test_hash_type_md2_lookup(self):
        assert_equals(HashType.MD2, HashType['MD2'])

    def test_hash_type_md2_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD2.hash_byte_length())

    def test_hash_type_md2_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD2.hash_str_length())

    def test_hash_type_md4_in_hash_type(self):
        assert_true('MD4' in HashType.__members__)

    def test_hash_type_md4_lookup(self):
        assert_equals(HashType.MD4, HashType['MD4'])

    def test_hash_type_md4_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD4.hash_byte_length())

    def test_hash_type_md4_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD4.hash_str_length())

    def test_hash_type_md5_in_hash_type(self):
        assert_true('MD5' in HashType.__members__)

    def test_hash_type_md5_lookup(self):
        assert_equals(HashType.MD5, HashType['MD5'])

    def test_hash_type_md5_has_hash_byte_length_16(self):
        assert_equals(16, HashType.MD5.hash_byte_length())

    def test_hash_type_md5_has_hash_str_length_32(self):
        assert_equals(32, HashType.MD5.hash_str_length())

    def test_hash_type_sha1_in_hash_type(self):
        assert_true('SHA1' in HashType.__members__)

    def test_hash_type_sha1_lookup(self):
        assert_equals(HashType.SHA1, HashType['SHA1'])

    def test_hash_type_sha1_has_hash_byte_length_20(self):
        assert_equals(20, HashType.SHA1.hash_byte_length())

    def test_hash_type_sha1_has_hash_str_length_40(self):
        assert_equals(40, HashType.SHA1.hash_str_length())

    def test_hash_type_sha224_in_hash_type(self):
        assert_true('SHA224' in HashType.__members__)

    def test_hash_type_sha224_lookup(self):
        assert_equals(HashType.SHA224, HashType['SHA224'])

    def test_hash_type_sha224_has_hash_byte_length_28(self):
        assert_equals(28, HashType.SHA224.hash_byte_length())

    def test_hash_type_sha224_has_hash_str_length_56(self):
        assert_equals(56, HashType.SHA224.hash_str_length())

    def test_hash_type_sha256_in_hash_type(self):
        assert_true('SHA256' in HashType.__members__)

    def test_hash_type_sha256_lookup(self):
        assert_equals(HashType.SHA256, HashType['SHA256'])

    def test_hash_type_sha256_has_hash_byte_length_32(self):
        assert_equals(32, HashType.SHA256.hash_byte_length())

    def test_hash_type_sha256_has_hash_str_length_64(self):
        assert_equals(64, HashType.SHA256.hash_str_length())

    def test_hash_type_sha384_in_hash_type(self):
        assert_true('SHA384' in HashType.__members__)

    def test_hash_type_sha384_lookup(self):
        assert_equals(HashType.SHA384, HashType['SHA384'])

    def test_hash_type_sha2384_has_hash_byte_length_48(self):
        assert_equals(48, HashType.SHA384.hash_byte_length())

    def test_hash_type_sha2384_has_hash_str_length_96(self):
        assert_equals(96, HashType.SHA384.hash_str_length())

    def test_hash_type_sha512_in_hash_type(self):
        assert_true('SHA512' in HashType.__members__)

    def test_hash_type_sha512_lookup(self):
        assert_equals(HashType.SHA512, HashType['SHA512'])

    def test_hash_type_sha512_has_hash_byte_length_64(self):
        assert_equals(64, HashType.SHA512.hash_byte_length())

    def test_hash_type_sha256_has_hash_str_length_128(self):
        assert_equals(128, HashType.SHA512.hash_str_length())
