import sqlite3
import re
import emoji
import pygame

class Bak():

    regex = re.compile(":.*?:")
    @staticmethod
    def select_names(namedb, table):
        load_tasks_query = "SELECT name FROM " + table
        my_tasks = Bak.runQuery(load_tasks_query, receive=True, namedb=namedb)
        return my_tasks

    @staticmethod
    def runQuery(sql,data=None, receive=False,namedb=None):
        conn = sqlite3.connect(namedb)
        print("连接成功...")
        cursor = conn.cursor()
        print("获取游标成功...")
        if data:
            print("存在传入数据...")
            cursor.execute(sql, data)
        else:
            print("正在执行sql语句...")
            cursor.execute(sql)
            print("执行sql语句成功...")

        if receive:
            print("成功返回了数据...")
            return cursor.fetchall()
        else:
            conn.commit()

        conn.close()

    @staticmethod
    def filter_emoji(desstr,restr=''):
        #过滤表情
        try:
            co = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        return co.sub(restr, desstr)
    @staticmethod
    def name_emoji(text):
        return emoji.demojize(text)
    @staticmethod
    def regex_clear(text):
        return Bak.regex.sub("",text)
    @staticmethod
    def play_music(q):
        filepath = "../bak/djproject.mp3";
        pygame.mixer.init()
        # 加载音乐
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play(start=0.0)
        # 播放时长，没有此设置，音乐不会播放，会一次性加载完
        # time.sleep(300)
        while True:
            if q.get() is None:
                break
        pygame.mixer.music.stop()
if __name__ == '__main__':

    db_friend = ("get_friends.db","get_friends")
    names = Bak.select_names(*db_friend)
    datafriends = []
    for name in names:
       datafriends.append((Bak.regex_clear(Bak.name_emoji(name[0])).strip(),))
    print(datafriends)
