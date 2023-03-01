import math


a = float(input('Enter number a: '))
b = float(input('Enter number b: '))
c = float(input('Enter number c: '))

x1 = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
x2 = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)

print(x1)
print(x2)