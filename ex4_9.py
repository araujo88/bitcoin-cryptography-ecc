from ecc import PrivateKey
from helper import hash256, little_endian_to_int

passphrase = b'teste'
secret = little_endian_to_int(hash256(passphrase))
priv = PrivateKey(secret)
print(priv.point.address(testnet = True))

'''Address: mt4o1EhS4SCgZ6gZHXETpnakykTfaa1Acc'''
