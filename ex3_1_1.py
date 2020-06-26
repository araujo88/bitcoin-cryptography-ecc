from ecc import FieldElement, Point

prime=223
a=FieldElement(0,prime)
b=FieldElement(7,prime)
x=FieldElement(192,prime)
y=FieldElement(105,prime)

p1=Point(x,y,a,b)

print(p1+p1)

