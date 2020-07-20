#! python3

import redis

__redisClient = None


def init(config):
    global __redisClient
    if __redisClient:
        __redisClient.close()
        __redisClient = None

    if not config.redis: return
    # 建立与Redis的连接
    __redisClient = redis.Redis(host=config.redis['host'], port=config.redis['port'], password=config.redis['password'],
                                db=config.redis["database"])

    # 发一个测试指令，让redis立即建立连接
    __redisClient.set("test_key", "test_value")


def remove_device_info(log, device_id):
    # 组合key格式
    key = "user_device_info2_" + device_id
    # 删除命令
    num = __redisClient.delete(key)
    # 在输出框中写入key+num %s %d 占位符
    print("[redis-remove] key:%s count:%d" % (key, num))


# init(config)

def remove_user_info(log, user_id):
    key = "user_info5_" + user_id
    num = __redisClient.delete(key)
    log.write("[redis-remove] key:%s count:%d" % (key, num))


def remove_account_info(log, account_id):
    key = "account_info1_" + account_id
    num = __redisClient.delete(key)
    log.write("[redis-remove] key:%s count:%d" % (key, num))


def get_user_info(log, user_id):
    key = "user_info5_" + user_id
    num = __redisClient.hgetall(key)
    log.write(str(num))
    # 直接用get：外面key+内部键值对的key
    # getall：只需要外面key，可以展示出内部所有的内容
    # hgetall、hget:查找的速度更快，hashmap格式，需要根据实际情况判定


def remove_user_sign_info(log, user_id):
    key = "UserSign1::" + user_id
    num = __redisClient.delete(key)
    log.write(str(num))
