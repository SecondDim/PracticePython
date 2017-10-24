#! python3

import time


def run():
    '''
    perf_counter <not include> cpu sleep time
    > It does not include time elapsed during sleep.
    '''

    start_time = time.perf_counter()
    # do something
    complete_time = time.perf_counter()

    print('run time use perf_counter' + str(complete_time - start_time) + ' s')


if __name__ == '__main__':
    run()
    input("DONE")
