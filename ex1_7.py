from ecc import FieldElement

for prime in (7,11,17,31):
	print([pow(1,prime-1) for i in range(prime-1)])
