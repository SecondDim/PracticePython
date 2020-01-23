import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pwnable.kr", 9007))

while True:
    data = s.recv(2048)
    if data.startswith("N="):
        qus = data.strip().split(' ')
        qN = qus[0][2:]
        qC = qus[1][2:]
        print(qN)
        print(qC)

        # pattern = re.compile("/^[NC]{1}\=[0-9]*/g")
        # result = re.match(pattern, data)
        # print(result.group(0))
        # print(result.group(1))
    # pattern = re.compile("^N=([0-9]*) C=([0-9]*)$")
    # match1 = pattern1.match(str(data))
    # print(match1)

try:
    pass
except:
    pass
    # if you key [crtl + c] ,you can terminal the script.
