import datetime
import logging
import os
from Configuration import LOG_PATH


def write(level, content):
    if not isinstance(content, str):
        try:
            content = str(content)
        except:
            pass
    with open('./Log/log/{}'.format(datetime.date.today()), 'a+') as f:
        f.write('[{}][{}]{}'.format(level, datetime.datetime.now(), content.encode('utf-8')))
        f.write('\n')


def space():
    with open('./Log/log/{}'.format(datetime.date.today()), 'a+') as f:
        f.write('\n')


def get_logger(name, sign, module='Other'):
    print('[LOGER] name:{}, sign:{}, module:{}'.format(name,sign,module))
    log_name = LOG_PATH + '{}-{}'.format(datetime.date.today(), module)
    try:
        handler = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024)
    except FileNotFoundError:
        os.mkdir('Log/log/')
        handler = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024)

    formatter = logging.Formatter(
        '[%(levelname)s] [{}] [%(asctime)s] %(filename)s - %(funcName)s : %(message)s'.format(sign))
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger
