#! python3

import time


def run():
    '''
    process_time <include> cpu sleep time
    > It does include time elapsed during sleep and is system-wide.
    '''

    start_time = time.process_time()
    # do something
    complete_time = time.process_time()

    print('run time use process_time' + str(complete_time - start_time) + ' s')


if __name__ == '__main__':
    run()
    input("DONE")
