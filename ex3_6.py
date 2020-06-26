from ecc import S256Point, G, N

px = 0x887387e452b8eacc4acfde10d9aaf7f6d9a0f975aabb10d006e4da568744d06c # Public key x point
py = 0x61de6d95231cd89026e286df3b6ae4a894a3378e393e93a0f45b666329a0ae34 # Public key y point

z = 0xec208baa0fc1c19f708a9ca96fdeff3ac3f230bb4a7ba4aede4942ad003c0f60 # Hash
r = 0xac8d1c87e51d0d441be8b3dd5b05c8795b48875dffe00b7ffcfac23010d3a395 # Signature x point
s = 0x68342ceff8935ededd102dd876ffd6ba72d6a427a3edb13d26eb0781cb423c4 # Signature y point

point = S256Point(px,py)
s_inv = pow(s, N-2, N) # Fermat's Little Theorem (N is prime)
u = z * s_inv % N # u = z/s
v = r * s_inv % N # v = r/s
print((u*G + v*point).x.num == r) # Checks if x coordinate is r
