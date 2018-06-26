Python 3.6.6rc1 (v3.6.6rc1:1015e38be4, Jun 12 2018, 08:38:06) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=2577
>>> b=2577
>>> a==b
True
>>> a is b
False
>>> print("string"+1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print("string"+1)
TypeError: must be str, not int
>>> print("string"+str(10))
string10
>>> print("string"*3)
stringstringstring
>>> print(3*"string")
stringstringstring
>>> print("string"*"string")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print("string"*"string")
TypeError: can't multiply sequence by non-int of type 'str'
>>> "walkwel">"walkwel"
False
>>> "a">"b"
False
>>> "ashu"<"bikram"
True
>>> "A"<="c"
True
>>> ord("A")
65
>>> ord("c")
99
>>> chr("a")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    chr("a")
TypeError: an integer is required (got type str)
>>> chr(96)
'`'
>>> chr(97)
'a'
>>> "a"=="b"
False
>>> "a"!="b"
True
>>> not(True)
False
>>> not("a"<="b" and "b">"c")
True
>>> name="abc"
>>> "a" in name
True
>>> "ab" in name
True
>>> "ab" not in name
False
>>> "ac" in name
False
>>> "b" in name
True
>>> "" in name
True
>>> str=None
>>> "" in str
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    "" in str
TypeError: argument of type 'NoneType' is not iterable
>>> 
