import logging
import datetime

def get_logging():
    logging.basicConfig(filename='log/{}'.format(datetime.date.today()), level=logging.INFO)
    return logging