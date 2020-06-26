from ecc import PrivateKey

priv = PrivateKey(5000)
print(priv.point.sec(compressed = False).hex())

priv = PrivateKey(2018**5)
print(priv.point.sec(compressed = False).hex())

priv = PrivateKey(0xdeadbeef12345)
print(priv.point.sec(compressed = False).hex())
