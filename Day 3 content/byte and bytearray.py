Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=[1,2,3,4]
>>> b=bytes(list)
>>> b
b'\x01\x02\x03\x04'
>>> for n in b:
	print(n)

1
2
3
4
>>> b[0]=1
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b[0]=1
TypeError: 'bytes' object does not support item assignment
>>> list=[1,1.2,1.2]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b=bytes(list)
TypeError: 'float' object cannot be interpreted as an integer
>>> list=[1.2,1.2]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b=bytes(list)
TypeError: 'float' object cannot be interpreted as an integer
>>> list=[450,1]
>>> b=bytes(list)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b=bytes(list)
ValueError: bytes must be in range(0, 256)
>>> b=bytearray(list)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b=bytearray(list)
ValueError: byte must be in range(0, 256)
>>> list=[1,2,3]
>>> b=bytearray(list)
>>> for n in b:
	print(n)

1
2
3
>>> b[0]=12
>>> for n in b:
	print(n)

12
2
3
>>> 
