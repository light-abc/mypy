from multiprocessing import Pool
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time, os, math
from joblib import Parallel, delayed, parallel_backend
import heartrate


def f_IO(a):  # IO 密集型
    time.sleep(5)

def f_compute(a):  # 计算密集型
    for _ in range(int(1e7)):
        math.sin(40) + math.cos(40)
    return

def normal(sub_f):
    for i in range(6):
        sub_f(i)
    return

def joblib_process(sub_f):
    with parallel_backend("multiprocessing", n_jobs=6):
        res = Parallel()(delayed(sub_f)(j) for j in range(6))
    return


def joblib_thread(sub_f):
    with parallel_backend('threading', n_jobs=6):
        res = Parallel()(delayed(sub_f)(j) for j in range(6))
    return

def mp(sub_f):
    with Pool(processes=6) as p:
        res = p.map(sub_f, list(range(6)))
    return

def asy(sub_f):
    with Pool(processes=6) as p:
        result = []
        for j in range(6):
            a = p.apply_async(sub_f, args=(j,))
            result.append(a)
        res = [j.get() for j in result]

def thread(sub_f):
    threads = []
    for j in range(6):
        t = Thread(target=sub_f, args=(j,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def thread_pool(sub_f):
    with ThreadPoolExecutor(max_workers=6) as executor:
        res = [executor.submit(sub_f, j) for j in range(6)]

def process_pool(sub_f):
    with ProcessPoolExecutor(max_workers=6) as executor:
        res = executor.map(sub_f, list(range(6)))

def showtime(f, sub_f, name):
    start_time = time.time()
    f(sub_f)
    print("{} time: {:.4f}s".format(name, time.time() - start_time))

def main(sub_f):
    showtime(normal, sub_f, "normal")
    print()
    print("------ 多进程 ------")
    showtime(joblib_process, sub_f, "joblib multiprocess")
    showtime(mp, sub_f, "pool")
    showtime(asy, sub_f, "async")
    showtime(process_pool, sub_f, "process_pool")
    print()
    print("----- 多线程 -----")
    showtime(joblib_thread, sub_f, "joblib thread")
    showtime(thread, sub_f, "thread")
    showtime(thread_pool, sub_f, "thread_pool")


if __name__ == "__main__":
    print("----- 计算密集型 -----")
    sub_f = f_compute
    heartrate.trace(main(sub_f))
    print()
    print("----- IO 密集型 -----")
    sub_f = f_IO
    heartrate.trace(main(sub_f))