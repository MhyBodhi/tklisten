import sqlite3,os
import time
import tkinter as tk
import tkinter.messagebox as msg
#解决数据依赖问题，便于开发
from select import Bak
from wxpy import Bot

class Basic(tk.Tk):

    def __init__(self):
        super().__init__()
        self.v_tuling = tk.StringVar(self)
        self.v_documents = tk.StringVar(self)
        self.v_services = tk.StringVar(self)

        #机器人对象,有的微信无法登陆，所以我这里禁掉了
        # self.bot = Bot(cache_path=True)  # <请将这部分注释解开.....>

        #变量定义
        self.chats = set()
        #一
        self.basic_frame = tk.Frame(self,bg="#8A2BE2")
        # self.basic_frame.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
        self.basic_frame.bind("<1>",self.reset)
        self.basic_frame.bind("<3>",self.reset)

        self.bg_frame = tk.Frame(self)
        self.bg_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.photo = tk.PhotoImage(file=r"C:\Users\mhy\Desktop\tkwxotpro\tk\bases\ok.gif")
        self.bg_label = tk.Label(self.bg_frame,image=self.photo,text="请点击扫码登陆微信",fg="green",compound = tk.CENTER,font=("华文行楷",20))
        self.bg_label.place(relx=0,rely=0,relheight=1,relwidth=1)


        #二
        self.login_button = tk.Button(self.bg_frame,bg="#4B0082",fg="black",text="登陆",command=self.login)
        self.login_button.place(relx=0.42,rely=0.55,relheight=0.1,relwidth=0.2)
        #二
        self.basic_listbox = tk.Listbox(self.basic_frame, height=24,width=30,selectmode=tk.EXTENDED)
        self.basic_listbox.place(x=0,y=30)
        self.information = ["1、支持群聊、好友自动聊天功能","2、支持下载手机群聊、好友文件","3、提供服务监控功能"]
        for data in self.information:
            self.basic_listbox.insert(tk.END,data)
        self.scrollbar = tk.Scrollbar(self.basic_frame, orient="vertical", command=self.basic_listbox.yview)
        self.basic_listbox["yscrollcommand"]=self.scrollbar.set
        self.scrollbar.pack(side="right",fill="y")
        #绑定事件
        self.basic_listbox.bind("<ButtonPress-1>",self.listenBases)
        self.basic_listbox.bind("<Control-a>",self.listenBases)
        self.basic_listbox.bind("<Shift-Button-1>",self.listenBases)

        #群聊
        self.group = tk.Button(self.basic_frame,bg="green",fg="black",text="群聊",command=self.display_groups)
        self.group.place(x=0,y=0)
        #好友
        self.friend = tk.Button(self.basic_frame,bg="green",fg="black",text="好友",command=self.display_friends,anchor="w")
        self.friend.place(x=29,y=0)
        #设置主窗体
        self.title("木火应")
        x = self.winfo_screenmmwidth()
        y = self.winfo_screenheight()
        self.geometry("500x500+%d+%d" % (x, y / 2 * 0.5))
        self.resizable(0,0)
        self.datafriends,self.datagroups = ([],[])
        #显示列表
        self.v = tk.StringVar(self.basic_frame)
        self.display = tk.Label(self.basic_frame,bg="green", fg="black", textvariable=self.v)
        #聊天机器人
        self.tulingbtn = tk.Button(self.basic_frame,textvariable=self.v_tuling,bg="#00FA9A",fg="black",stat="disable",command=self.tuling)
        self.v_tuling.set("聊天机器人")
        self.tulingbtn.place(x=215,y=100)
        #收集聊天文件
        self.documentsbtn = tk.Button(self.basic_frame,textvariable=self.v_documents,bg="#00FF7F",fg="black",stat="disable",command=self.documents)
        self.v_documents.set("收集聊天文件")
        self.documentsbtn.place(x=215,y=150)
        #服务监控
        self.servicesbtn = tk.Button(self.basic_frame,textvariable=self.v_services,bg="#66CDAA",fg="black",stat="disable",command=self.service)
        self.v_services.set("微信服务监控")
        self.servicesbtn.place(x=215,y=200)
        #隐藏self.basic_frame
        self.basic_frame.pack_forget()
        # self.update_image()

    def chatTuling(self):
        raise Exception
    def reset(self,event):
        raise Exception
    def documents(self):
        raise Exception
    def tuling(self):
        raise Exception
    def service(self):
        raise  Exception
    def listenBase(self,event):
        raise Exception
    def logout(self):
        raise Exception

    def tips(self):
        self.basic_listbox.delete(0, tk.END)
        self.basic_listbox.insert(tk.END,"微信掉线，正重新登陆！")
        self.friend["stat"] = "disable"
        self.group["stat"] = "disable"

    def display_friends(self):
        self.tulingbtn["stat"] = "active"
        self.documentsbtn["stat"] = "active"
        self.servicesbtn["stat"] = "active"
        if len(self.datafriends)>0 or len(self.datagroups)>0:
            self.basic_listbox.delete(0, tk.END)
            self.v.set("好友列表")
            self.display.place(x=90,y=0,height=30)
            self.friend["stat"] = "disable"
            self.group["stat"] = "active"
            for friend in self.datafriends:
                if friend:
                    self.basic_listbox.insert(tk.END, friend[0])
            return True
        else:
            self.tips()
            self.login()

    def display_groups(self):
        self.tulingbtn["stat"] = "active"
        self.documentsbtn["stat"] = "active"
        self.servicesbtn["stat"] = "active"
        if len(self.datafriends)>0 or len(self.datagroups)>0:
            self.basic_listbox.delete(0, tk.END)
            self.v.set("群聊列表")
            self.display.place(x=90, y=0,height=30)
            self.friend["stat"] = "active"
            self.group["stat"] = "disable"
            for group in self.datagroups:
                if group:
                    self.basic_listbox.insert(tk.END,group[0])
            return True
        else:
            self.tips()
            self.login()

    def login(self):

        try:
            #这部分由于我个人微信无法登陆，仅解决数据依赖问题，真实情况注释就行
            db_friend = ("get_friends.db", "get_friends")
            names = Bak.select_names(*db_friend)
            self.datafriends = []
            for name in names:
                self.datafriends.append((Bak.regex_clear(Bak.name_emoji(name[0])).strip(),))

            #真实环境
            # self.datafriends = self.friends()
            self.datagroups = self.groups()
        except:
            pass
        if len(self.datafriends)>0 or len(self.datagroups)>0:
            self.login_button.pack_forget()
            self.bg_frame.pack_forget()
            self.basic_frame.pack(side=tk.TOP,fill=tk.BOTH,expand=1)
            self.logout_button = tk.Button(self.basic_frame,width=10,text="退出",bg="red",fg="black",command=self.logout)
            self.logout_button.place(x=400,y=5)
            self.friend["stat"] = "active"
            self.group["stat"] = "active"
            self.basic_listbox.delete(0, tk.END)
            self.basic_listbox.insert(0, "恭喜，登陆成功！")
            return True
        else:
            msg.showerror("提示","登陆失败，请稍后再试！")
            return False


    def friends(self):
        db_friend = (self.friends.__name__ + ".db", self.friends.__name__)
        if os.path.exists(db_friend[0]):
            names = self.load_tasks(*db_friend)
            if names[0][0]== self.bot.self.nick_name:
                return names
            else:
                os.remove(db_friend[0])
                return self.init_friend(db_friend)
        return self.init_friend(db_friend)
    def init_friend(self,db_table):
        names = []
        friends = self.bot.getAllFriends()
        for friend in friends:
            names.append(Bak.regex_clear(Bak.name_emoji(friend.nick_name)).strip())
        Basic.connectDB(*db_table)
        for name in iter(names):
            self.save_task(*db_table,name)
        names = self.load_tasks(*db_table)
        return names

    def init_group(self,db_table):
        names = []
        groups = self.bot.getAllGroups()
        for group in groups:
            names.append(Bak.regex_clear(Bak.name_emoji(group.nick_name)).strip())
        Basic.connectDB(*db_table)
        for name in iter(names):
            self.save_task(*db_table,name)
        names = self.load_tasks(*db_table)
        return names

    def groups(self):
        # db_group = (self.groups.__name__ + ".db", self.groups.__name__)
        # if os.path.exists(db_group[0]):
        #     names = self.load_tasks(*db_group)
        #     if names[0][0] == self.bot.self.nick_name:
        #         return names
        #     else:
        #         os.remove(db_group[0])
        #         return self.init_friend(db_group)
        # return self.init_group(db_group)

        return [("group"+str(i),) for i in range(1,10)]



    def members(self):
        pass

    def save_task(self, namedb,table,task):

        insert_task_query = "INSERT INTO " + table + " VALUES (?)"
        insert_task_data = (task,)
        self.runQuery(insert_task_query, insert_task_data,namedb=namedb)

    def load_tasks(self,namedb,table):
        load_tasks_query = "SELECT name FROM " + table
        my_tasks = self.runQuery(load_tasks_query, receive=True,namedb=namedb)
        return my_tasks

    def delete_tasks(self,namedb,table,text):
        delete_task_query = "DELETE FROM " + table + " WHERE name=?"
        delete_task_data = (text.cget("text"),)
        self.runQuery(delete_task_query, delete_task_data,namedb=namedb)
    def delete_all(self):
        dbs = [self.friends.__name__ + ".db",self.groups.__name__ + ".db"]
        # try:
        #     for db in dbs:
        #         os.remove(db)
        # except:
        #     pass


    @staticmethod
    def runQuery(sql, data=None, receive=False,namedb=None):
        conn = sqlite3.connect(namedb)
        cursor = conn.cursor()
        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)

        if receive:
            return cursor.fetchall()
        else:
            conn.commit()

        conn.close()

    @staticmethod
    def connectDB(namedb,table):
        create_tables = "CREATE TABLE " + table + "(name TEXT)"
        Basic.runQuery(create_tables,namedb=namedb)

if __name__ == '__main__':
    Basic = Basic()
    # Basic.login()
    Basic.mainloop()
