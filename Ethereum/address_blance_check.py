#! python3

# xcode-select --install
# or
# sudo apt-get install python3-dev
# and
# pip install web3

from web3 import Web3, HTTPProvider

import sys

address_list = []
percent = 1000000000000000000

mainnet_rpc = "http://localhost:8545"  # mainnet
rinkeby_rpc = "http://localhost:8545"  # rinkeby
byb_rpc = "http://localhost:8545"  # byb

mainnet_w3 = Web3(HTTPProvider(mainnet_rpc))
for x in mainnet_w3.eth.accounts:
    address_list.append(x)

rinkeby_w3 = Web3(HTTPProvider(rinkeby_rpc))
for x in rinkeby_w3.eth.accounts:
    address_list.append(x)

# byb_w3 = Web3(HTTPProvider(byb_rpc))
# for x in byb_w3.eth.accounts:
#     address_list.append(x)


def help():
    print("""
    description
        Check eth address total balance.

    example
        [script] amr

    argv
        h  : show this help
        A  : show all address balance. default False.
        a  : show all address balance if balance higher then zero. default False.
        m  : check main net. default True.
        r  : check rinkeby net. default False.
    """)


def mainnet(show_all_not_zero, show_all):
    total_balance = 0
    for address in address_list:
        while True:
            try:
                balance = mainnet_w3.eth.getBalance(address)
            except ConnectionError:
                print("[X] mainnet_rpc connect error, try again.")
                continue
            break
        total_balance = total_balance + balance
        if show_all_not_zero:
            if balance > 0:
                print(address + " : " + str(balance/percent) + " ETH")
        elif show_all:
            print(address + " : " + str(balance/percent) + " ETH")

    print("\nMainNet, Total balance : " +
          str(total_balance/percent) + " ETH\n")


def rinkeby(show_all_not_zero, show_all):
    total_balance = 0
    for address in address_list:
        balance = rinkeby_w3.eth.getBalance(address)
        total_balance = total_balance + balance
        if show_all_not_zero:
            if balance > 0:
                print(address + " : " + str(balance/percent) + " ETH")
        elif show_all:
            print(address + " : " + str(balance/percent) + " ETH")

    print("\nRinkeby, Total balance : " +
          str(total_balance/percent) + " ETH\n")


def byb(show_all_not_zero, show_all):
    total_balance = 0
    for address in address_list:
        balance = byb_w3.eth.getBalance(address)
        total_balance = total_balance + balance
        if show_all_not_zero:
            if balance > 0:
                print(address + " : " + str(balance/percent) + " BYB")
        elif show_all:
            print(address + " : " + str(balance/percent) + " BYB")

    print("\Byb, Total balance : " +
          str(total_balance/percent) + " BYB\n")


def main(argv):

    show_all_not_zero = False
    show_all = False

    if "a" in argv:
        show_all_not_zero = True

    if "A" in argv:
        show_all = True

    # byb(show_all_not_zero, show_all)

    if "m" in argv:
        mainnet(show_all_not_zero, show_all)

    if "r" in argv:
        rinkeby(show_all_not_zero, show_all)
        pass


if __name__ == '__main__':

    argv = ["m"]

    if len(sys.argv) == 1:
        main(argv)

    elif len(sys.argv) == 2:
        if "h" in sys.argv[1]:
            help()
            sys.exit(0)

        if "a" in sys.argv[1]:
            argv.append("a")
        if "A" in sys.argv[1]:
            argv.append("A")
        if "r" in sys.argv[1]:
            argv.append("r")

        main(argv)

    else:
        print("  argv error!  ")
