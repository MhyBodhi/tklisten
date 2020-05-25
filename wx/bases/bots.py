import time
from wxpy import *
class Bots(Bot):
    def __init__(self,cache_path=True,login_callback=None,logout_callback=None,puid_path='wxpy_puid.pkl'):
        Bot.__init__(self,cache_path=cache_path,login_callback=login_callback,logout_callback=logout_callback)
        self.enable_puid(puid_path)

    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    def fileHelper(self):
        return self.file_helper

def catch_exception(origin_func):
    def wrapper(self, *args, **kwargs):
        try:
            u = origin_func(self, *args, **kwargs)
            return u
        except Exception:
            # self.revive() #不用顾虑，直接调用原来的类的方法
            return 'an Exception raised.'
    return wrapper

if __name__ == '__main__':
    bot = Bots()