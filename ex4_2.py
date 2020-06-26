from ecc import PrivateKey

priv = PrivateKey(5001)
print(priv.point.sec(compressed = True).hex())

priv = PrivateKey(2019**5)
print(priv.point.sec(compressed = True).hex())

priv = PrivateKey(0xdeadbeef54321)
print(priv.point.sec(compressed = True).hex())
