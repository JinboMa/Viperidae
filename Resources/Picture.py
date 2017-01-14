import datetime
import os
from Handler.LoginRequireHandler import LoginRequireHandler
import base64
from Log.logger import get_logger


class Picture(LoginRequireHandler):
    class_name = 'Picture'

    def prepare(self):
        self.logger = get_logger(self.class_name, self.sign)
        super(Picture, self).prepare()

    def post(self, *args, **kwargs):
        try:
            picture = self.get_argument('picture')
            self.logger.info('get picture success, picture is:{}'.format(picture))

            original_image = base64.b64decode(self.complete_picture(picture))

            path = 'Resources/{}'.format(self.user_id)

            self.logger.info('prepare to save picture, path:{}'.format(path))

            # 如果没有这个路径 进行创建操作
            if not os.path.exists(path):
                self.logger.info('path is not exist, mkdir:{}'.format(path))
                os.mkdir(path)

            file_name = path + '/{}'.format(self.get_name())

            with open(file_name, 'wb+') as f:
                f.write(original_image)
                self.logger.info('save picture success, name:{}'.format(file_name))

            self.result['result'] = True
            self.result['message']['path'] = file_name

        except Exception as e:
            self.logger.error(str(e))
            self.result['result'] = False
            self.result['message']['error'] = str(e)
        finally:
            self.finish(self.result)

    def get_name(self):
        # 获取图片名称（根据时间，精确到ms）
        t = datetime.datetime.now()
        return str(t.year) + str(t.month) + str(t.day) + \
               str(t.hour) + str(t.minute) + str(t.second) + str(t.microsecond)

    def complete_picture(self, picture):
        # 补全图片（base64格式字符串长度需要是4的倍数，如果不够需用'='补齐）
        if (len(picture) % 4) == 0:
            self.logger.info('picture length is suitable, return original picture')
            return picture
        else:
            miss = 4 - (len(picture) % 4)
            picture += '=' * miss
            self.logger.info('picture length is not suitable, complete picture:{}'.format(picture))
            return picture
