import sys
print(sys.argv)

C:\Users\HP\Desktop>py parm.py 1 2 3 4
parm.py

C:\Users\HP\Desktop>py parm.py 1 2 3 4
1

C:\Users\HP\Desktop>py parm.py 1 2 3 4
['1', '2', '3', '4']

C:\Users\HP\Desktop>py parm.py Walk Wel
['Walk', 'Wel']

C:\Users\HP\Desktop>py parm.py Walk Wel
['parm.py', 'Walk', 'Wel']

C:\Users\HP\Desktop>py parm.py "Walk Well"
['parm.py', 'Walk Well']

C:\Users\HP\Desktop>py parm.py 'walwel walk'
['parm.py', "'walwel", "walk'"]

C:\Users\HP\Desktop>py parm.py """walk well"""
['parm.py', '"walk well"']

C:\Users\HP\Desktop>py parm.py '''walkwel well'''
['parm.py', "'''walkwel", "well'''"]

C:\Users\HP\Desktop>
