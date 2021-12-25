# time for work:  44 sec 1-core
# 13 sec - multicore
import time
import multiprocessing
from multiprocessing import Manager
from multiprocessing import Process


# Multicore version
def loop(number, dict):
    result_number = []
    for i in range(1, number + 1):
        if number % i == 0:
            result_number.append(i)
    dict[number] = result_number


def factorize(*numbers):
    processes = []
    manager = Manager()
    m = manager.dict()
    for number in numbers:
        p1 = Process(target=loop, args=(number, m))
        p1.start()
        processes.append(p1)
    for p in processes:
        p.join()

    return m


'''
Single-core version


def factorize(*numbers):
    result = []
    for number in numbers:
        result_number = []
        for i in range(1, number+1):
            if number % i == 0:
                result_number.append(i)
        result.append(result_number)
    return result

'''
if __name__ == '__main__':
    start_time = time.time()
    multiprocessing.set_start_method('spawn')
    result_dict = factorize(106510602, 106510664, 106510645, 10651060,
                            106510601, 106510664, 106510645, 106510664, 106510645)
    print('time for work: ', time.time()-start_time)
