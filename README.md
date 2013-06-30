StructClass
===========

This Python module allows to manipulate binary packed objects as classes.

Similarly to the standard library struct module, objects can be packed or unpacked.

Usage example
-------------

    >>> from structclass import StructClass
    >>> SomePacket = StructClass('SomePacket', '<II', ['length', 'age'])
    >>> my_packet = SomePacket.unpack(b'12345678')[0]
    >>> my_packet
    SomePacket(length=875770417, age=943142453)
    >>> my_packet.age
    943142453
    >>> my_packet.pack()
    b'12345678'
