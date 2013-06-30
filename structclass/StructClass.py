"""
This module allows to manipulate binary packed objects as classes.

Similarly to the standard library struct module, objects can be or unpacked.
"""

import struct

__author__ = 'David Berthelot'


def StructClass(name, format, fields, defaults={}):
    """
    :name:      The name of the class to create
    :format:    The struct format (refer to the standard struct module documentation)
    :fields:    The list of field names corresponding to the struct entries
    :defaults:  An optional dictionary of default value for some or all of the fields
    """
    class StructClass(object):
        _FORMAT = format
        _FIELDS = fields

        def __init__(self, **entries):
            for field in self._FIELDS:
                self.__dict__[field] = entries.get(field, defaults.get(field))

        def pack(self):
            return struct.pack(self._FORMAT, *([self.__dict__[field] for field in self._FIELDS]))

        @classmethod
        def unpack(cls, input_bytes):
            packsize = struct.calcsize(cls._FORMAT)
            entries = {field: value for field, value in zip(cls._FIELDS, struct.unpack(cls._FORMAT, input_bytes)[:packsize])}
            return cls(**entries), input_bytes[packsize:]

        def __repr__(self):
            return self.__class__.__name__+'('+', '.join([field+'='+repr(self.__dict__[field]) for field in self._FIELDS])+')'
    StructClass.__name__ = name
    return StructClass
            
