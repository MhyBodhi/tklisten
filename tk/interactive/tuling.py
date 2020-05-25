import time
import json
import tkinter as tk
import requests
from bases.bsservices import BsService


class TuLing(BsService):
    def __init__(self):
        super().__init__()
        self.text_api_error = tk.StringVar(self)
        self.label_api_error = tk.Label(self.basic_frame,textvariable=self.text_api_error,fg="red",bg="#8A2BE2", font=("黑体", 10))
        #隐藏
        self.label_api_error.place_forget()
    def startChat(self):
        self.label_api_error.place_forget()
        if self.chats_listbox.size()==0:
            self.text_api_error.set("监控列表不能为空...")
            self.label_api_error.place(x=280, y=60, width=150, height=20)
            return

        self.entry_tulingapi.place_forget()
        self.label_showapi.place_forget()
        self.startchatbtn.place_forget()
        self.cancelchatbtn.place_forget()

        # key="720b8495c39f40ac92284c5d6b3d1dd7"
        # {"code":40001,"text":"亲爱的，key不对哦。"}
        #获取图灵api
        tuling_api = self.tuling_api.get()
        #测试是否可用
        url = "http://www.tuling123.com/openapi/api?key={key}&info={msg}".format(key=tuling_api,msg="测试")
        status_code = json.loads(requests.get(url=url).text)["code"]
        status_text = json.loads(requests.get(url=url).text)["text"]
        if status_code >=100000 and status_text != "对不起，没听清楚，请再说一遍吧。":
            print(self.bot.getSomeFriends(self.chats))
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
        return TuLing()
if __name__ == '__main__':
    # key="720b8495c39f40ac92284c5d6b3d1dd7"
    # # {"code":40001,"text":"亲爱的，key不对哦。"}
    # #
    # url = "http://www.tuling123.com/openapi/api?key={key}&info={msg}".format(key=key, msg="测试")
    # res = requests.get(url=url)
    # res.encoding = "utf-8"
    # print(json.loads(res.text))

    base = TuLing()
    base.mainloop()