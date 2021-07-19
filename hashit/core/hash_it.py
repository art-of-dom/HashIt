"""
hash_type.py
The heavy hitter of hashing.
"""
from __future__ import absolute_import

import six

from hashit.core.mappings.hashlib_mapping import HASHLIB_MAPPING
from hashit.core.mappings.custom_crc_mapping import CRCMOD_CUSTOM_MAPPING


class HashIt(object):
    """The object to preform hashing"""

    def __init__(self, hash_type=None, hash_data=None):
        self.hash_type = hash_type
        self.data = hash_data

    def next_chunk(self):
        """Hash the next chunk of data"""
        return self._hash(self.data.next_chunk())

    def hash_it(self, hash_type=None, hash_data=None):
        """Hash all of the data"""
        if hash_type is not None:
            self.hash_type = hash_type

        if hash_data is not None:
            self.data = hash_data

        return self._hash(self.data.next_chunk())

    def _hash(self, data):
        """Internal hashing mapping"""
        hash_str = ""
        data = self._sanatize_data(data)

        if self.hash_type in HASHLIB_MAPPING:
            hash_str = self._hashlib_hash(data)
        elif self.hash_type in CRCMOD_CUSTOM_MAPPING:
            hash_str = hex(CRCMOD_CUSTOM_MAPPING[self.hash_type](data))[
                2:].upper()
        else:
            raise NotImplementedError
        return hash_str

    @staticmethod
    def _sanatize_data(data):
        """Temporary py2/py3 data helper"""
        if six.PY3:
            try:
                data = data.encode('utf-8')
            except (UnicodeDecodeError, AttributeError):
                pass
        else:
            data = str(data)
        return data

    def _hashlib_hash(self, data):
        """Internal hashing mapping specifically for hashlib like interfaces"""
        hasher = HASHLIB_MAPPING[self.hash_type]()
        hasher.update(data)
        return hasher.hexdigest().upper()
