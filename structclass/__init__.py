"""
This module allows to manipulate binary packed objects as classes.

Similarly to the standard library struct module, objects can be or unpacked.

Usage example:
>>> from structclass import StructClass
>>> SomePacket = StructClass('SomePacket', '<II', 'length age'.split())
>>> my_packet, extra = SomePacket.unpack(b'123456789a')[0]
>>> my_packet
SomePacket(length=875770417, age=943142453)
>>> my_packet.age
943142453
>>> my_packet.pack()
b'12345678'
>>> extra
b'9a'
>>> # Extra contains the bytes not used

"""

__title__ = 'structclass'
__version__ = '1.0.2'
__author__ = 'David Berthelot'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 ' + __author__

from .StructClass import StructClass
