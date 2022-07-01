import os
from random import randint
import threading
import time
from threading import Thread
from multiprocessing import Pool
import csv
import shutil

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'
RESULTS = []

def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1

def func1(array: list):
    return fib(array)

def play_func1(listFib: list,callable:list):
    for i in range(len(callable)):
        file = 'output/'+str(callable[i])+'.txt'
        with open(file, 'w+') as f:
            f.write(str(listFib[i]))

def func2(result_file: str,callable:list):
    f = open(result_file, 'w+', encoding='UTF8')
    writer = csv.writer(f)
    for i in callable:
        with open(f'output/{i}.txt') as f:
            contents = int(f.read())
            writer.writerow([str(i),str(contents)])

if __name__ == '__main__':

    shutil.rmtree(OUTPUT_DIR)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    starttime = time.time()
    callable_list = list(set([randint(1000, 100000) for _ in range(1000)]))
    endtime = time.time()
    print(f"Time taken {endtime - starttime} seconds")
    starttime = time.time()
    pool = Pool()
    list_fib =pool.map(func1, callable_list)
    pool.close()
    play_func1(list_fib,callable_list)
    func2(RESULT_FILE,callable_list)
    endtime = time.time()
    print(f"Time taken {endtime - starttime} seconds")

    #func2(result_file=RESULT_FILE)
