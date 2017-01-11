import datetime
import os
from Handler.LoginRequireHandler import LoginRequireHandler
import base64

from Log.logger import get_logger


class Picture(LoginRequireHandler):
    class_name = 'Picture'

    def prepare(self):
        self.logger = get_logger(self.class_name)
        super(Picture, self).prepare()

    def post(self, *args, **kwargs):
        try:
            picture = self.get_argument('picture')
            print(len(picture))
            miss = 4 - (len(picture) % 4)
            picture += '=' * miss
            original_image = base64.b64decode(picture)

            path = 'Resources/{}'.format(self.user_id)
            if not os.path.exists(path):
                os.mkdir(path)

            file_name = path + '/{}'.format(self.get_name())

            with open(file_name, 'wb+') as f:
                f.write(original_image)

            self.result['result'] = True
            self.result['message']['path'] = file_name

        except Exception as e:
            self.logger.error(str(e))
            self.result['result'] = False
            self.result['message']['error'] = str(e)
        finally:
            self.finish(self.result)

    def get_name(self):
        t = datetime.datetime.now()
        return str(t.year) + str(t.month) + str(t.day) + \
               str(t.hour) + str(t.minute) + str(t.second) + str(t.microsecond)
