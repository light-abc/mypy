#!/usr/bin/env python

import redis
from rediscluster import  RedisCluster

def replcinfo():
    rc = RedisCluster([{'host': '192.168.0.105', 'port': 6380},
                       {'host': '192.168.0.105', 'port': 6381},
                       {'host': '192.168.0.105', 'port': 6382}])

    r = redis.StrictRedis(host='192.168.0.105', port=6380, db=1)
    rs = redis.StrictRedis(host='192.168.0.105', port=26380, db=1)
    print(rs.info("replication"))
    # info = r.info("replication")
    # print(info)
    rs.close()

if __name__ == '__main__':
    replcinfo()