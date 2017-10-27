#! python3
# -*- coding: utf-8 -*-

import hashlib
import binascii


def run():

    test_str = b'Hello World.'

    m = hashlib.sha3_256(test_str).digest()

    print(binascii.hexlify(m))


if __name__ == '__main__':
    run()

    inp = input("DONE")
