from bases.basic import Basic,tk
from tkinter.ttk import Separator

class BsTuLing(Basic):

    def __init__(self):
        super().__init__()
        # 监控列表容器
        self.chats_listbox = tk.Listbox(self.basic_frame,selectmode=tk.EXTENDED)

        # 滚动条
        self.chat_scrollbar = tk.Scrollbar(self.chats_listbox, orient="vertical", command=self.chats_listbox.yview)
        self.chats_listbox.config(yscrollcommand=self.chat_scrollbar.set)

        # 显示
        self.monitoring = tk.Label(self.basic_frame, text="监控对象列表", fg="blue", bg="#8A2BE2", font=("黑体", 10))

        # 图灵api输入框
        self.tuling_api = tk.StringVar(self)
        self.entry_tulingapi = tk.Entry(self.basic_frame, textvariable=self.tuling_api)
        self.tuling_api.set("请输入图灵api")

        # 提示
        self.label_showapi = tk.Label(self.basic_frame, text="图灵api:", bg="#8A2BE2", font=("黑体", 10))

        # 开启聊天按钮
        self.startchatbtn = tk.Button(self.basic_frame, text="开始聊天", bg="green", command=self.startChat)

        # 取消聊天
        self.cancelchatbtn = tk.Button(self.basic_frame, text="取消", bg="red", command=self.cancelChat)

        # 绑定事件
        self.chats_listbox.bind("<ButtonPress-1>", self.listenChats)
        self.chats_listbox.bind("<Control-a>", self.listenChats)
        self.chats_listbox.bind("<Shift-Button-1>", self.listenChats)

        #全部控件处于于隐藏
        self.chats_listbox.place_forget()
        self.chat_scrollbar.place_forget()
        self.monitoring.place_forget()
        self.entry_tulingapi.place_forget()
        self.label_showapi.place_forget()
        self.startchatbtn.place_forget()
        self.cancelchatbtn.place_forget()

        #功能指针
        self.status = 0
        #取消指针
        self.tuling_cancel = 0
        self.document_cancel = 0
        self.service_cancel = 0
    def tuling(self):
        self.status = 1
        self.tuling_cancel = 1
        self.chats_listbox.place(relx=0.45, rely=0.55, relheight=0.3, relwidth=0.3)
        self.chat_scrollbar.pack(side="right", fill="y")
        self.monitoring.place(relx=0.45, rely=0.50)
        self.entry_tulingapi.place(x=280, y=78)
        self.label_showapi.place(x=215, y=80)
        self.startchatbtn.place(x=309, y=100)
        self.cancelchatbtn.place(x=380, y=100)
        self.dataExchange()

    def dataExchange(self):

        self.basic_indexs = self.basic_listbox.curselection()
        self.chats_indexs = self.chats_listbox.curselection()
        if self.basic_indexs:
            for index in self.basic_indexs:
                base_data = self.basic_listbox.get(index)
                if base_data:
                    self.chats.add(base_data)
                # 从群聊或好友列表中删除聊天对象
                self.basic_listbox.delete(index)
            # 更新监控列表
            self.chats_listbox.delete(0,tk.END)
            for chat in self.chats:
                self.chats_listbox.insert(0, chat)
            return
        if self.chats_indexs:
            for index in self.chats_indexs:
                self.chats.discard(self.chats_listbox.get(index))
                # 向群聊或好友列表中增加聊天对象
                chat_data = self.chats_listbox.get(index)
                if chat_data:
                    self.basic_listbox.insert(tk.END,chat_data)
            #更新监控列表
            self.chats_listbox.delete(0,tk.END)
            for chat in self.chats:
                self.chats_listbox.insert(0, chat)
            return

    def listenBases(self,event):
        if self.status==0:
            pass
        elif self.status==1:
            self.v_tuling.set("添加聊天对象")
            self.v_documents.set("收集聊天文件")
            self.v_services.set("微信监控服务")
            self.tulingbtn["stat"] = "active"
            self.documentsbtn["stat"] = "disable"
            self.servicesbtn["stat"] = "disable"
        elif self.status==2:
            self.v_documents.set("添加聊天对象")
            self.v_tuling.set("聊天机器人")
            self.v_services.set("微信监控服务")
            self.documentsbtn["stat"] = "active"
            self.tulingbtn["stat"] = "disable"
            self.servicesbtn["stat"] = "disable"
        elif self.status==3:
            self.v_services.set("添加聊天对象")
            self.v_documents.set("收集聊天文件")
            self.v_tuling.set("聊天机器人")
            self.servicesbtn["stat"] = "active"
            self.documentsbtn["stat"] = "disable"
            self.tulingbtn["stat"] = "disable"

    def listenChats(self,event):
        if self.status==1:
            self.v_tuling.set("删除聊天对象")
            self.v_documents.set("收集聊天文件")
            self.v_services.set("微信监控服务")
            self.tulingbtn["stat"] = "active"
            self.documentsbtn["stat"] = "disable"
            self.servicesbtn["stat"] = "disable"
        elif self.status==2:
            self.v_documents.set("删除聊天对象")
            self.v_tuling.set("聊天机器人")
            self.v_services.set("微信监控服务")
            self.documentsbtn["stat"] = "active"
            self.tulingbtn["stat"] = "disable"
            self.servicesbtn["stat"] = "disable"
        elif self.status==3:
            self.v_services.set("删除聊天对象")
            self.v_documents.set("收集聊天文件")
            self.v_tuling.set("聊天机器人")
            self.servicesbtn["stat"] = "active"
            self.documentsbtn["stat"] = "disable"
            self.tulingbtn["stat"] = "disable"
        return
    def reset(self,event):
        self.chats_listbox.selection_clear(0,tk.END)
        self.basic_listbox.selection_clear(0,tk.END)
        self.resetStatus()
    def resetStatus(self):
        self.v_documents.set("收集聊天文件")
        self.documentsbtn["stat"] = "active"
        self.v_tuling.set("聊天机器人")
        self.tulingbtn["stat"] = "active"
        self.v_services.set("微信监控服务")
        self.servicesbtn["stat"] = "active"
    def cancelChat(self):
        # 重置取消按钮状态
        self.tuling_cancel = 0
        #隐藏公有元素
        self.hide_public_elements((self.document_cancel,))
        #隐藏私有元素
        self.entry_tulingapi.place_forget()
        self.label_showapi.place_forget()
        self.startchatbtn.place_forget()
        self.cancelchatbtn.place_forget()
        #重置功能按钮状态
        self.resetStatus()
        #交回添加删除归属权
        if self.status == 1:
            self.status = 0

    def hide_public_elements(self,cancels):
        # 隐藏监控列表-->公有元素
        if False not in [cancel==0 for cancel in cancels]: #& self.service_cancel == 0
            for data in self.chats:
                self.basic_listbox.insert(tk.END,data)
            self.chats.clear()
            self.chats_listbox.delete(0, tk.END)
            self.status = 0
            self.chats_listbox.place_forget()
            self.chat_scrollbar.place_forget()
            self.monitoring.place_forget()

    def startChat(self):
        raise Exception

if __name__ == '__main__':
    tuling = BsTuLing()
    tuling.mainloop()


