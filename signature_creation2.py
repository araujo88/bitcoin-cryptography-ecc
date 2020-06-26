from ecc import PrivateKey
from hashlib import sha256

password = 'my secret'
message = 'my message'

e = int.from_bytes(sha256(password.encode('utf-8')).digest(), 'big')
z = int.from_bytes(sha256(message.encode('utf-8')).digest(), 'big')

print(e)
print(z)

signature = PrivateKey.sign(e, z)

print(signature)


