# immutable vs mutable

# ways to declare string
str='this is string'
str1="this is string 2"
string3="""this is
 
mutiline"""

# using index
# +ve index
print(str[0])
# -ve index
print(str[-1])
# substring using slice operator
print(str[0:3])
# len of string
print(len(str))
# slice varitaions
print(str[0:])
print(str[:3])
print(str[0:14:])
print(str[0:14:2])
print(str[::])
# immutable barhaviour of string
# str[0]='1'
