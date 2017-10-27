# pytohn3
# -*- coding: utf8 -*-
'''
    預設即為utf8
    沒有 u'中文' 這種用法了(因為預設STR就是用unicode儲存)
'''

'''
    http://blog.chunnorris.cc/2015/04/python-2x-unicode.html
    bytes decode()
    str   encode()
    https://docs.python.org/3/howto/unicode.html
    https://docs.python.org/2/howto/unicode.html

    「unicode 物件」透過 encode(encoding) 變成「str 物件」(i.e. a sequence of bytes)
    「str 物件」透過 decode(encoding) 變成「unicode 物件」

    可以用中文當變數名稱

    s = "a\xac\u1234\u20ac\U00008000"
    #     ^^^^ two-digit hex escape
    #         ^^^^^^ four-digit Unicode escape
    #                     ^^^^^^^^^^ eight-digit Unicode escape

    chr()
    ord()
 '''


def run_encode(msg):

    print(msg)
    print(type(msg))
    print(len(msg))
    # print(msg.decode('utf8'))
    print(msg.decode('cp950'))
    print(msg.decode('big5'))

    print(msg.encode('utf8'))
    print(msg.encode('cp950'))
    print(msg.encode('big5'))
    # print(msg.encode('ascii'))

    # print(msg.encode('utf8').hex())
    # print(msg.encode('hex'))


def run():
    # msg = "中文行不行？"
    # msg = b'\xe4\xb8\xad\xe6\x96\x87\xe8\xa1\x8c\xe4\xb8\x8d\xe8\xa1\x8c\xef\xbc\x9f'
    # msg = "Hello World!"
    # msg = b'\x48\x65\x6c\x6c\x6f'
    msg = b'\xa4\xa4\xa4\xe5'
    # msg = '\u5566'
    # msg = "中文"
    # 變數 = "!!!!!"

    run_encode(msg)


if __name__ == '__main__':
    run()

    # inp = input("DONE")
