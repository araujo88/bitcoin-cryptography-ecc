from ecc import encode_base58

h1 = bytes.fromhex("7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d")
h2 = bytes.fromhex("eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c")
h3 = bytes.fromhex("c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6")

print(encode_base58(h1))
print(encode_base58(h2))
print(encode_base58(h3))
