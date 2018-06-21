Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> complex(1)
(1+0j)
>>> complex(0b0101)
(5+0j)
>>> complex(1,5)
(1+5j)
>>> complex(0b1111,0b1111)
(15+15j)
>>> comlex=0b1111+0b1111
>>> complex=0b111+0b111j
SyntaxError: invalid syntax
>>> comlex(1.1,1.1)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    comlex(1.1,1.1)
TypeError: 'int' object is not callable
>>> complex(1,1.1)
(1+1.1j)
>>> complex(1.1,1)
(1.1+1j)
>>> comlex("False")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    comlex("False")
TypeError: 'int' object is not callable
>>> complex("False")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    complex("False")
ValueError: complex() arg is a malformed string
>>> 
