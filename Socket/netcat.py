# pylint: disable-all
# flake8: noqa

""" https://gist.github.com/Integralist/36621860135c2a265cf7b6eb0f661db5 """

import sys
import socket
import getopt
import threading
import subprocess

listen = command = upload = False
execute = target = upload_destination = ''
port = 0


def usage():
    print '''
        netcat.py -t <host> -p <port>
        -l, --listen                (listen on specified host/port)
        -e, --execute=<file_to_run> (execute file upon connection)
        -c, --command               (initialize a shell)
        -u, --upload=<destination>  (upload file upon connection)
    '''


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))

        if len(buffer):
            client.send(buffer)

        while True:
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print response

            buffer = raw_input('')
            buffer += '\n'

            client.send(buffer)
    except:
        print 'Exception. Exiting'
        client.close()


def server_loop():
    global target

    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(
            target=client_handler,
            args=(client_socket,)
        )
        client_thread.start()


def run_command(cmd):
    command = cmd.rstrip()

    try:
        output = subprocess.check_output(
            command,
            stderr=subprocess.STDOUT,
            shell=True
        )
    except:
        output = 'Failed to execute command\r\n'

    return output


def client_handler(client_socket):
    global upload, execute, command

    if len(upload_destination):
        file_buffer = ''

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(upload_destination, 'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send(
                'Successfully saved file to {}\r\n'.format(upload_destination))
        except:
            client_socket.send(
                'Failed to save file to {}\r\n'.format(upload_destination))

    if len(execute):
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            client_socket.send('<BHP:#> ')
            cmd_buffer = ''

            while '\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            response = run_command(cmd_buffer)
            client_socket.send(response)


def main():
    global listen, port, execute, command, upload_destination, target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:', [
            'help', 'listen', 'execute', 'target', 'port', 'command', 'upload'
        ])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--command'):
            command = True
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read(
        client_sender(buffer)

    if listen:
        server_loop()

main()

"""
echo -ne 'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n' | python netcat.py -t www.google.com -p 80
also
python netcat.py -l -p 9999 -c        # first  terminal
python netcat.py -t localhost -p 9999 # second terminal
"""
