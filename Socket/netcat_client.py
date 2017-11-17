#! python3

import socket


class Netcat:

    """ Python 'netcat like' module """
    """ https://gist.github.com/leonjza/f35a7252babdf77c8421 """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length=1024):
        """ Read 1024 bytes off the socket """

        return self.socket.recv(length).decode("utf8")

    def read_until(self, data):
        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024).decode("utf8")

        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]

        return rval

    def write(self, data):

        self.socket.send(data)

    def close(self):

        self.socket.close()


def run(argv):
    ip = argv[1]
    port = int(argv[2])

    nc = Netcat(ip, port)

    while True:
        recv = nc.read_until('\n')  # windows \n\t
        print(recv)

    nc.close()


if __name__ == '__main__':
    import sys
    import re

    if len(sys.argv) != 3:
        print("Need Arg like [IPv4] [port]")
    elif re.match(r'^[1-255].[1-255].[1-255].[1-255]$', sys.argv[1]):
        print("IPv4 format error")
    elif int(sys.argv[2]) < 0 or int(sys.argv[2]) > 65535:
        print("Port Range need in 1-65535")
    else:
        run(sys.argv)
