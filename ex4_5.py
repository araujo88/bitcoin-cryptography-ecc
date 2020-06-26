from ecc import PrivateKey

priv = PrivateKey(5002)
print(priv.point.address(compressed=False, testnet=True))

priv = PrivateKey(2020**5)
print(priv.point.address(compressed=True, testnet=True))

priv = PrivateKey(0x12345deadbeef)
print(priv.point.address(compressed=True, testnet=False))
