#! pytohn3

from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA

message = b"Hello"
key = ElGamal.generate(256, Random.new().read)
h = SHA.new(message).digest()
while 1:
    k = random.StrongRandom().randint(1, key.p - 1)
    if GCD(k, key.p - 1) == 1:
        break
sig = key.sign(h, k)
...
if key.verify(h, sig):
    print("OK")
else:
    print("Incorrect signature")
