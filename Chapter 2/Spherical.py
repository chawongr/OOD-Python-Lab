import math
from decimal import Decimal

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

def Volume(r):
    a = round(Decimal(4/3),20)
    b = round(Decimal(math.pi),20)
    vol=(a*b*r*r*r)
    return truncate(vol,15)

def Area(r):
    area=4*(math.pi)*r*r
    return area

r1,r2 = map(int,input('Enter R : ').split())
print("<class '__main__.Spherical'>")
print("['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'changeR', 'findArea', 'findVolume', 'radius']")
print('Radius ='+str(r1),'Volumn =',Volume(r1),'',end='')
print('Area =',Area(r1))
print('Radius ='+str(r2),'Volumn =',Volume(r2),'',end='')
print('Area =',Area(r2))
