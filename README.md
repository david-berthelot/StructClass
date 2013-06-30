StructClass
===========

This Python module allows to manipulate binary packed objects as classes.

Similarly to the standard library struct module, objects can be packed or unpacked.

Usage example
-------------

    >>> from structclass import StructClass
    >>> SomePacket = StructClass('SomePacket', '<II', ['length', 'age'])
    >>> my_packet, extra = SomePacket.unpack(b'123456789a')
    >>> my_packet
    SomePacket(length=875770417, age=943142453)
    >>> my_packet.age
    943142453
    >>> my_packet.pack()
    b'12345678'
    >>> extra
    b'9a'
    >>> # Extra contains the bytes not used during unpacking
