import datetime


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
