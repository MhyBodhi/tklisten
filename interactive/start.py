import sys
sys.path.append(r"C:\\Users\mhy\\Desktop\\project\\wxlisten")
import os
import time
import json
import tkinter as tk
import _tkinter
from multiprocessing import Process,Queue
from interactive.documentready import DocumentReady
from bak.select import Bak
from wxpy import *
import requests
class Start(DocumentReady):
    def __init__(self):
        super().__init__()
        self.display_frame =  tk.Frame(self,bg="lime")
        self.cv = tk.Canvas(self.display_frame,width=200,height=200,bg="lime",border=0,highlightthickness=0)
        self.cv_ol = self.cv.create_oval(1,1,198,198,fill="#EE82EE",outline="#EE82EE")
        self.collect_files = tk.Label(self.display_frame,bg="lime",text="收集的文件在:C:\\userfiles目录下...")
        self.collect_files.place(relx=0.3,rely=0.12)
        self.label_cv_text = tk.StringVar(self)
        self.label_cv = tk.Label(self.cv,textvariable=self.label_cv_text,fg="black",bg="#EE82EE",font=("微软雅黑",20))
        self.label_cv_text.set("监控中")
        self.label_cv.place(relx=0.3,rely=0.3)
        self.cv.place(relx=0.3, rely=0.3)
        #文字指针
        self.words_status = 0
        self.word_status_0_4 = True
        self.colors= ["Violet", "Magenta", "Fuchsia", "DarkMagenta", "Purple", "MediumOrchid", "DarkViolet", "DarkOrchid",
                  "Indigo", "BlueViolet", "MediumPurple", "SlateBlue", "DarkSlateBlue", "Lavender", "GhostWhite",
                  "Blue", "MediumBlue", "MidnightBlue", "DarkBlue", "Navy",'RoyalBlue', 'CornflowerBlue', 'LightSteelBlue',
                  'LightSlateGray', 'SlateGray', 'DodgerBlue', 'AliceBlue', 'SteelBlue', 'LightSkyBlue', 'SkyBlue', 'DeepSkyBlue',
                'LightBlue', 'PowderBlue', 'CadetBlue', 'Azure', 'LightCyan', 'PaleTurquoise', 'Cyan', 'Aqua', 'DarkTurquoise',
                'DarkSlateGray', 'DarkCyan', 'Teal', 'MediumTurquoise', 'LightSeaGreen', 'Turquoise', 'Aquamarine', 'MediumAquamarine',
                'MediumSpringGreen', 'MintCream', 'SpringGreen', 'MediumSeaGreen', 'SeaGreen', 'Honeydew', 'LightGreen', 'PaleGreen',
                'DarkSeaGreen', 'LimeGreen', 'Lime', 'ForestGreen', 'Green', 'DarkGreen', 'Chartreuse', 'LawnGreen', 'GreenYellow',
                'DarkOliveGreen', 'YellowGreen', 'OliveDrab', 'Beige', 'LightGoldenrodYellow', 'Ivory', 'LightYellow', 'Yellow',
                'Olive', 'DarkKhaki', 'LemonChiffon', 'PaleGoldenrod', 'Khaki', 'Gold', 'Cornsilk', 'Goldenrod', 'DarkGoldenrod',
                'FloralWhite', 'OldLace', 'Wheat', 'Moccasin', 'Orange']
        #颜色指针
        self.color_index = 0
        self.color_status_0_86 = True
    def displayColor(self):
        self.cv.itemconfigure(self.cv_ol, outline=self.colors[self.color_index], fill=self.colors[self.color_index])
        self.label_cv.configure(bg=self.colors[self.color_index])
        
        if self.words_status == 0:
            self.label_cv_text.set("监控中.")
        elif self.words_status == 1:
            self.label_cv_text.set("监控中..")
        elif self.words_status == 2:
            self.label_cv_text.set("监控中...")
        elif self.words_status == 3:
            self.label_cv_text.set("监控中....")
        else:
            self.label_cv_text.set("监控中.....")

        if self.word_status_0_4:
            self.words_status += 1
        else:
            self.words_status -= 1
            
        if self.words_status == 4:
            self.word_status_0_4 = False
        if self.words_status == 0:
            self.word_status_0_4 = True

        if self.color_status_0_86:
            self.color_index += 1
        else:
            self.color_index -= 1

        if self.color_index == 0:
            self.color_status_0_86 = True
        elif self.color_index == 86:
            self.color_status_0_86 =False

        self.after(30,self.displayColor)
    def start(self):
        self.basic_frame.pack_forget()

        self.display_frame.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        self.chatTuling(self.chats,self.get_tuling_api)
        # t = Process(target=self.chatTuling, args=(self.chats, self.get_tuling_api))
        # t.start()

    def chatTuling(self,friends_groups,tulinapi):
	
        bot = self.bot # <请将这部分注释解开.....>


        class Chats():

            @classmethod
            def getInstance(cls, *args, **kwargs):
                if not hasattr(Chats, "_instance"):
                    Chats._instance = bot
                return Chats._instance

            def __init__(self):
                self.bot = bot

            def getTime(self):
                return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

            # friends
            def getAllFriends(self):
                try:
                    return self.bot.friends()
                except Exception as e:
                    logging.warning("获取全部好友失败", e)
                    return False

            def getSomeFriends(self, names):
                somefriend = []
                try:
                    for name in names:
                        somefriend.extend(self.getOneFriend(name))
                    return somefriend
                except Exception as e:
                    logging.warning("获取部分好友失败", e)
                    return False

            def getOneFriend(self, name):
                onefriend = []
                try:
                    friends = self.bot.friends()
                    for friend in friends:
                        if Bak.regex_clear(Bak.name_emoji(friend.nick_name).strip()) == name:
                            onefriend.append(friend)
                    return onefriend
                except Exception as e:
                    logging.info("获取一个好友失败", e)
                    raise

            # groups
            def getAllGroups(self):
                try:
                    return self.bot.groups()
                except Exception as e:
                    logging.warning("获取全部群组失败", e)
                    return False

            def getSomeGroups(self, names):
                somegroups = []
                try:
                    for name in names:
                        somegroups.extend(self.getOneGroup(name))
                    return somegroups
                except Exception as e:
                    logging.warning("获取部分群组失败", e)
                    return False

            def getOneGroup(self, name):
                onegroup = []
                try:
                    groups = self.bot.groups()
                    for group in groups:
                        if name == Bak.regex_clear(Bak.name_emoji(group.nick_name).strip()):
                            onegroup.append(group)
                    return onegroup
                except Exception as e:
                    logging.info("获取一个群组失败", e)
                    raise

            # members
            def getAllMembers(self, group):
                try:
                    group = ensure_one(self.bot.groups().search(group))
                    return group.members
                except Exception as e:
                    logging.warning("获取全部群友失败", e)
                    return False

            def getSomeMembers(self, group, names):
                listMembers = []
                try:
                    group = ensure_one(self.bot.groups().search(group))
                    for name in names:
                        listMembers.extend(self.getOneMember(name))
                    return listMembers
                except Exception as e:
                    logging.warning("获取部分群友失败", e)
                    return False

            def getOneMember(self, group, name):
                onemember = []
                try:
                    group = ensure_one(self.bot.groups().search(group))
                    for member in group.members:
                        if name == Bak.regex_clear(Bak.name_emoji(member.nick_name).strip()):
                            onemember.append(member)
                    return onemember
                except Exception as e:
                    logging.info("获取一个群友失败", e)
                    raise

        base = Chats()
        friends = base.getSomeFriends(friends_groups)
        groups = base.getSomeGroups(friends_groups)
        all = friends.extend(groups)

        # 主要聊天功能...
        @bot.register(chats=all,msg_types=TEXT)
        def tuling_chat(msg):

            url = "http://www.tuling123.com/openapi/api?key={key}&info={msg}".format(key=tulinapi, msg=msg.text)
            text = json.loads(requests.get(url=url).text)["text"]
            msg.reply(text)

        # 文件收集功能 ---
        @bot.register(chats=all,msg_types=[PICTURE,RECORDING,VIDEO],except_self=False)
        def collect_files(msg):
            name = Bak.regex_clear(Bak.name_emoji(msg.sender.nick_name)).strip()
            filepath = "C:\\userfiles\\" + name + "\\"
            if not os.path.exists("C:\\userfiles"):
                os.mkdir("C:\\userfiles")
            if not os.path.exists(filepath):
                os.mkdir(filepath)
            msg.get_file(save_path=filepath + msg.file_name)

        embed()


    def logout(self):
        self.destroy()
        return Start()

    @staticmethod
    def play_music(q):
        Bak.play_music(q)

    def run(self):
            p = Process(target=self.play_music,args=(q,))
            p.start()
            self.after(50,self.displayColor)
            self.mainloop()

if __name__ == '__main__':
    q = Queue()
    base = Start()
    base.run()
    while True:
        try:
            q.put(1)
            base.state()
        except _tkinter.TclError:
            q.put(None)
            break


