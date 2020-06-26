from ecc import FieldElement

p = 31
a = FieldElement(3,p)
b = FieldElement(24,p)
c = FieldElement(17,p)
d = FieldElement(4,p)

print(a/b)
print(c**-3)
