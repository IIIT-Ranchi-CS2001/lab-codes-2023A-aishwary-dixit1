import math

a = int(input('1st side'))
b = int (input('2nd side'))
c = int(input('3rd side'))

s = float((a+b+c)/2)

area =math.sqrt((s)(s-a)(s-b)*(s-c))
print(f"area of traingle is {area}")