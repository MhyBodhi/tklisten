import time
import json
import tkinter as tk
import tkinter.font as tf
import requests
from PIL import Image,ImageTk
from bases.bsservices import BsService

class ChatReady(BsService):
    def __init__(self):
        super().__init__()
        #验证api提示信息
        self.text_api_error = tk.StringVar(self)
        self.label_api_error = tk.Label(self.basic_frame,textvariable=self.text_api_error,fg="red",bg="#8A2BE2", font=("黑体", 10))

        #聊天初始化
        self.chat_ready = tk.Label(self.basic_frame,text="聊天准备就绪...",fg="black",bg="#8A2BE2", font=("黑体", 12))
        #取消准备按钮
        self.cancel_tuling_start = tk.Button(self.basic_frame,text="取消准备",fg="black",bg="red", font=("黑体", 10),command=self.cancelStart)

        #激活按钮
        self.startbtu = tk.Button(self.basic_frame,relief="sunken",fg="black",stat="disable",bg="red",text="开始",font=("微软雅黑",12,tf.BOLD),command=self.start)
        self.startbtu.place(relx=0.77, rely=0.65, relheight=0.1, relwidth=0.1)

        #隐藏
        self.label_api_error.place_forget()
        self.chat_ready.place_forget()
        self.cancel_tuling_start.place_forget()

        #图灵就绪指针
        self.tuling_ready_status = 0
        #文件收集就绪指针
        self.document_ready_status = 0
    def start(self):
        raise Exception
    def cancelChat(self):
        super().cancelChat()
        self.label_api_error.place_forget()
    def cancelCollect(self):
        super().cancelCollect()
        self.label_api_error.place_forget()
    def cancelStart(self):
        self.tuling_ready_status = 0
        if self.tuling_ready_status == 1 or self.document_ready_status == 1:
            self.startbtu.configure(bg="green", relief="raised", stat="active")
        else:
            self.startbtu.configure(bg="red", relief="sunken", stat="disable")
        self.chats_listbox.place(relx=0.45, rely=0.55, relheight=0.3, relwidth=0.3)
        self.monitoring.place(relx=0.45, rely=0.50)
        self.tulingbtn.place(x=215, y=100)
        self.cancelchatbtn.place(x=380, y=100)
        self.entry_tulingapi.place(x=280, y=78)
        self.label_showapi.place(x=215, y=80)
        self.startchatbtn.place(x=309, y=100)

        self.chat_ready.place_forget()
        self.cancel_tuling_start.place_forget()
    def tuling(self):
        super().tuling()
        self.label_api_error.place_forget()
    def startChat(self):
        self.label_api_error.place_forget()
        if self.chats_listbox.size()==0:
            self.text_api_error.set("监控对象列表不能为空")
            self.label_api_error.place(x=280, y=60, width=150, height=20)
            return

        self.entry_tulingapi.place_forget()
        self.label_showapi.place_forget()
        self.startchatbtn.place_forget()
        self.cancelchatbtn.place_forget()
        # {"code":40001,"text":"亲爱的，key不对哦。"}
        #获取图灵api
        self.get_tuling_api = self.tuling_api.get()
        #测试是否可用
        url = "http://www.tuling123.com/openapi/api?key={key}&info={msg}".format(key=self.get_tuling_api,msg="测试")
        status_code = json.loads(requests.get(url=url).text)["code"]
        status_text = json.loads(requests.get(url=url).text)["text"]
        if status_code <=100000 and status_text != "对不起，没听清楚，请再说一遍吧。":
            self.tuling_ready_status = 1
            #判断是否全部出于就绪状态
            if self.tuling_ready_status == 1 and self.document_ready_status == 1:
                self.chats_listbox.place_forget()
                self.monitoring.place_forget()
            self.tulingbtn.place_forget()
            self.chat_ready.place(x=215, y=100)
            self.cancel_tuling_start.place(x=380, y=100)
            self.startbtu.configure(bg="green",relief="raised",stat="active")


        else:
            self.text_api_error.set("api无效,请重新输入...")
            self.label_api_error.place(x=280, y=60, width=150, height=20)

            self.entry_tulingapi.place(x=280, y=78)
            self.label_showapi.place(x=215, y=80)
            self.startchatbtn.place(x=309, y=100)
            self.cancelchatbtn.place(x=380, y=100)
            pass
    def logout(self):
        self.destroy()
        return ChatReady()
if __name__ == '__main__':
    # # {"code":40001,"text":"亲爱的，key不对哦。"}
    # #
    # url = "http://www.tuling123.com/openapi/api?key={key}&info={msg}".format(key=key, msg="测试")
    # res = requests.get(url=url)
    # res.encoding = "utf-8"
    # print(json.loads(res.text))

    base = ChatReady()
    base.mainloop()