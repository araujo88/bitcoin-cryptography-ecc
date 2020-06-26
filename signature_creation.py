from ecc import S256Point, G, N
from hashlib import sha256

password = 'my secret'
message = 'my message'

e = int.from_bytes(sha256(password.encode('utf-8')).digest(), 'big')
z = int.from_bytes(sha256(message.encode('utf-8')).digest(), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
point = e*G
print(point)
print(hex(z))
print(hex(r))
print(hex(s))
