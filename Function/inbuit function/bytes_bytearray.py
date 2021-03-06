>>> bytes()     # output : b''
>>> bytearray()    # output : bytearray(b'')
>>> type(bytes())   # output : <class 'bytes'>
>>> type(bytearray()) # output : <class 'bytearray'>
# String
>>> bytes('hey','utf-8') # output : b'hey'
>>> bytes('hey','utf-16') # output : b'\xff\xfeh\x00e\x00y\x00'
>>> bytes('hey','utf-32') # output : b'\xff\xfe\x00\x00h\x00\x00\x00e\x00\x00\x00y\x00\x00\x00'
>>> bytes(1) # output : b'\x00'
>>> bytes(4) # output : b'\x00\x00\x00\x00'
# iterables
>>> bytes([1,2,3])  # output : b'\x01\x02\x03'
>>> bytearray([1,2,3]) # output : bytearray(b'\x01\x02\x03')
# diversion
>>> x = bytearray([1,2,3]) 
>>> x           # output : bytearray(b'\x01\x02\x03')
>>> x.append(1)
>>> x           # output : bytearray(b'\x01\x02\x03\x01')
>>> x.reverse()
>>> x  # output : bytearray(b'\x01\x03\x02\x01')
>>> y = bytes([1,2,3]) #diversion
>>> y   # output : b'\x01\x02\x03'

>>> y.append(4)    # we can't do it because bytes is immutable
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    y.append(4)    # we can't do it because bytes is immutable
AttributeError: 'bytes' object has no attribute 'append'
  
>>> x.append(4)
>>> x  # output : bytearray(b'\x01\x03\x02\x01\x04')





