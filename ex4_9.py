from ecc import PrivateKey
from helper import hash256, little_endian_to_int

passphrase = b'jiboiamutante'
secret = little_endian_to_int(hash256(passphrase))
priv = PrivateKey(secret)
print(priv.point.address(testnet = True))

'''Address: mkHc2s6q11EqgwLGdg9Adh6qM7C6yUfXqv'''
