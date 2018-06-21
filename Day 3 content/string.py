Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str="walkwel"
>>> str1="walkwel"
>>> id(str)
2071463671768
>>> id(str1)
2071463671768
>>> s[0]='d'
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s[0]='d'
NameError: name 's' is not defined
>>> str[0]='a'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    str[0]='a'
TypeError: 'str' object does not support item assignment
>>> str="xyz"
>>> id(str)
2071461983096
>>> str="xyz"
>>> id(str)
2071461983096
>>> str="xyz"
>>> id(str)
2071461983096
>>> str="abc"
>>> id(str)
2071452902768
>>> st="xyz"
>>> id(st)
2071463874488
>>> s="xyz"
>>> str="xyz"
>>> id(str)
2071463874488
>>> 
