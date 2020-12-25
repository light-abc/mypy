#!/usr/bin/env Python
# coding:utf-8
import sys
import time
import datetime
from rediscluster import StrictRedisCluster
import threading
from time import ctime, sleep


def redis_cluster_write():
    redis_nodes = [{'host': '192.168.0.105', 'port': 6380},
                   {'host': '192.168.0.105', 'port': 6381},
                   {'host': '192.168.0.105', 'port': 6382}]
    try:
        redis_conn = StrictRedisCluster(startup_nodes=redis_nodes, password='******')
    except Exception:
        raise Exception
    redis_conn.config_set('cluster-require-full-coverage', 'yes')
    counter = 0
    for i in range(0, 100000):
        counter = counter + 1
        redis_conn.set('key_' + str(i), 'value_' + str(i))
        # redis_conn.execute_command('wait', 1, 0)
        if counter == 1000:
            print('insert 1000 keys ' + str(str(datetime.datetime.now())))
            counter = 0


def redis_concurrence_test(thread_id):
    redis_nodes = [{'host': '192.168.0.105', 'port': 6380},
                   {'host': '192.168.0.105', 'port': 6381},
                   {'host': '192.168.0.105', 'port': 6382}]
    try:
        redis_conn = StrictRedisCluster(startup_nodes=redis_nodes, password='******')
    except Exception:
        raise Exception
    redis_conn.config_set('cluster-require-full-coverage', 'yes')
    counter = 0
    for i in range(0, 10000):
        counter = counter + 1
        redis_conn.set('key_' + str(thread_id) + '_' + str(counter), 'value_' + str(i))
        # redis_conn.execute_command('wait', 1, 0)
        if counter == 1000:
            print(str(thread_id) + ':insert 1000 keys ' + str(str(datetime.datetime.now())))
            counter = 0


if __name__ == '__main__':
    # redis_cluster_write()
    threads = []
    for i in range(10):
        t = threading.Thread(target=redis_concurrence_test, args=(i,))
        threads.append(t)
    begin_time = ctime()
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()