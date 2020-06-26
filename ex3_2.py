from ecc import FieldElement, Point

prime=223
a=FieldElement(0,prime)
b=FieldElement(7,prime)

x1, y1 = 170, 142
x2, y2 = 47, 71
x3, y3 = 17, 56
x4, y4 = 143, 98
x5, y5 = 76, 66
x6, y6 = 60, 139

p1=Point(FieldElement(x1,prime),FieldElement(y1,prime),a,b)
p2=Point(FieldElement(x2,prime),FieldElement(y2,prime),a,b)
p3=Point(FieldElement(x3,prime),FieldElement(y3,prime),a,b)
p4=Point(FieldElement(x4,prime),FieldElement(y4,prime),a,b)
p5=Point(FieldElement(x5,prime),FieldElement(y5,prime),a,b)
p6=Point(FieldElement(x6,prime),FieldElement(y6,prime),a,b)

print(p1+p6)
print(p2+p3)
print(p4+p5)

