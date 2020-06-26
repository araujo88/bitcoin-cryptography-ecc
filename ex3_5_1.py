from ecc import FieldElement, Point

prime=223
a=FieldElement(0,prime)
b=FieldElement(7,prime)
x=FieldElement(15,prime)
y=FieldElement(86,prime)

p=Point(x,y,a,b)
Inf=Point(None,None,a,b)
i=1
product=i*p

while product != Inf:
	product=i*p
	print(product)
	print(i)
	i+=1

