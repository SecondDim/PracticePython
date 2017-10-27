#! python3

import time


def loop():
    i = 100000
    while i:
        i = i - 1


def run():
    '''
    process_time <include> cpu sleep time
    > Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process.
    > (sum of mulit core process time)
    > It does include time elapsed during sleep and is system-wide.

    perf_counter <not include> cpu sleep time
    > Return the value (in fractional seconds) of a performance counter
    > It does not include time elapsed during sleep.
    '''

    pro_st = time.process_time()
    loop()
    pro_ed = time.process_time()

    per_st = time.perf_counter()
    time.sleep(1)
    per_ed = time.perf_counter()

    print('run time use process_time: ' + str(pro_ed - pro_st) + ' s')
    print('run time use perf_counter: ' + str(per_ed - per_st) + ' s')

    print('process_time_st: ' + str(pro_st))
    print('process_time_ed: ' + str(pro_ed))
    print('perf_counter_st: ' + str(per_st))
    print('perf_counter_ed: ' + str(per_ed))
    print('--------------------------------------------------')

    time.sleep(5)


if __name__ == '__main__':
    while True:
        run()
    input("DONE")
