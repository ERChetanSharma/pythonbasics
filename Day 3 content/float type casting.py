Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> float(1)
1.0
>>> float("1.2")
1.2
>>> float("0b10101.01010")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    float("0b10101.01010")
ValueError: could not convert string to float: '0b10101.01010'
>>> float("0b10101")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float("0b10101")
ValueError: could not convert string to float: '0b10101'
>>> float(True)
1.0
>>> float(1+2j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    float(1+2j)
TypeError: can't convert complex to float
>>> 
