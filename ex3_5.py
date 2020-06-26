from ecc import FieldElement, Point

prime=223
a=FieldElement(0,prime)
b=FieldElement(7,prime)
x=FieldElement(15,prime)
y=FieldElement(86,prime)

p=Point(x,y,a,b)
product=p
count=1
Inf=Point(None,None,a,b)

while product != Inf:
	product += p
	print(product)
	count += 1

print(product)
print(count)
