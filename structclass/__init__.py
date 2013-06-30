"""
This module allows to manipulate binary packed objects as classes.

Similarly to the standard library struct module, objects can be or unpacked.

Usage example:
>>> from structclass import StructClass
>>> SomePacket = StructClass('SomePacket', '<II', 'length age'.split())
>>> SomePacket.unpack(b'12345678')[0]
SomePacket(length=875770417, age=943142453)
>>> _.pack()
b'12345678'

"""

__title__ = 'structclass'
__version__ = '1.0.1'
__author__ = 'David Berthelot'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 ' + __author__

from .StructClass import StructClass
