import secrets
import time

# 賭輸加倍
principal = -1
f_stake = 1
l_stake = 0

count = 100 * 10000

print('[*] 1/2:')
stack = f_stake

# for x in range(count):

x=0
while True:
    x+=1
    if secrets.randbelow(100) < 50:
        stack = stack * 2
        if l_stake < stack:
            l_stake = stack
    else:
        stack = f_stake

    if (x % 100) == 0:
        print('[-] count: %s, maximum: %s' % (x, l_stake), end='\r')

    time.sleep(0.01)

print('')
print('[*] count: %s, maximum: %s' % (x, l_stake))
