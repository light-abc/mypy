#!/usr/bin/env Python
# coding:utf-8
import sys
import time
import datetime
from rediscluster import StrictRedisCluster
import threading
from time import ctime, sleep


def redis_cluster_write():
    redis_nodes = [{'host': '10.0.8.', 'port': 8888},
                   {'host': '172.18.0.12', 'port': 8888},
                   {'host': '172.18.0.13', 'port': 8888},
                   {'host': '172.18.0.14', 'port': 8888},
                   {'host': '172.18.0.15', 'port': 8888},
                   {'host': '172.18.0.16', 'port': 8888}]
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
    redis_nodes = [{'host': '172.18.0.11', 'port': 8888},
                   {'host': '172.18.0.12', 'port': 8888},
                   {'host': '172.18.0.13', 'port': 8888},
                   {'host': '172.18.0.14', 'port': 8888},
                   {'host': '172.18.0.15', 'port': 8888},
                   {'host': '172.18.0.16', 'port': 8888}]
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