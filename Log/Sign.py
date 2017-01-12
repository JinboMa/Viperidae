import datetime
import hashlib


def get_sign():
    way = hashlib.md5()
    way.update(str(datetime.datetime.now()).encode('utf-8'))
    return way.hexdigest()