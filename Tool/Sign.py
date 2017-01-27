import datetime
import hashlib


def get_sign():
    # 返回当前时间的md5值
    way = hashlib.md5()
    way.update(str(datetime.datetime.now()).encode('utf-8'))
    return way.hexdigest()
