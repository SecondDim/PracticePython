#! python3

import time


def run():
    '''
    process_time <include> cpu sleep time
    > It does include time elapsed during sleep and is system-wide.

    perf_counter <not include> cpu sleep time
    > It does not include time elapsed during sleep.
    '''

    pro_st = time.process_time()
    time.sleep(1)
    pro_ed = time.process_time()

    per_st = time.perf_counter()
    time.sleep(1)
    per_ed = time.perf_counter()

    print('run time use process_time: ' + str(pro_ed - pro_st) + ' s')
    print('run time use perf_counter: ' + str(per_ed - per_st) + ' s')
    print('pro_st: ' + str(pro_st))
    print('pro_ed: ' + str(pro_ed))
    print('per_st: ' + str(per_st))
    print('per_ed: ' + str(per_ed))
    print('--------------------------------------------------')


if __name__ == '__main__':
    while True:
        run()
    input("DONE")
