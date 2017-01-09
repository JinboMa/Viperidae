import datetime


def write(level, content):
    with open('./Log/log/{}'.format(datetime.date.today()), 'a') as f:
        f.write('[{}][{}]{}'.format(level, datetime.datetime.now(), content.encode('utf8')))
        f.write('\n')


def space():
    with open('./Log/log/{}'.format(datetime.date.today()), 'a') as f:
        f.write('\n')
