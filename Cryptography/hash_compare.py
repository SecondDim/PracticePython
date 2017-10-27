#! python3
# -*- coding: utf-8 -*-

import time
import binascii

test_str = b'Hello World.'

'''hashlib'''
import hashlib

per_st = time.perf_counter()

m = hashlib.sha256(test_str).digest()

per_ed = time.perf_counter()

print(binascii.hexlify(m))
print('run time use hashlib: ' + str(per_ed - per_st) + ' s')

'''pycryptodome'''
from Crypto.Hash import SHA256

per_st = time.perf_counter()
h = SHA256.new(test_str).digest()
per_ed = time.perf_counter()
print(binascii.hexlify(h))
print('run time use pycryptodome: ' + str(per_ed - per_st) + ' s')

'''cryptography'''
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

per_st = time.perf_counter()

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(test_str)
s = digest.finalize()

per_ed = time.perf_counter()

print(binascii.hexlify(s))
print('run time use cryptography: ' + str(per_ed - per_st) + ' s')
