#! python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # reuse tcp
sock.bind(('', 8787))
sock.listen(0)

while True:
    (csock, adr) = sock.accept()
    print("Client Info: ", csock, adr)
    msg = csock.recv(1024)
    if not msg:
        pass
    else:
        print("Client send: " + msg.decode("utf8"))
        csock.send(b"Hello I'm Server.\r\n" + msg)
    csock.close()
