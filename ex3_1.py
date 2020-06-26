from ecc import FieldElement, Point

a=0
b=7
prime=223
x1, y1 = 192, 105
x2, y2 = 17, 56
x3, y3 = 200, 119
x4, y4 = 1, 193
x5, y5 = 42, 99

p1=Point(FieldElement(x1,prime),FieldElement(y1,prime),FieldElement(a,prime),FieldElement(b,prime))
p2=Point(FieldElement(x2,prime),FieldElement(y2,prime),FieldElement(a,prime),FieldElement(b,prime))

print(p1+p2)

