from bases.bstuling import BsTuLing
import tkinter as tk
class BsDocuMents(BsTuLing):
    def __init__(self):
        super().__init__()
        # 开启收集按钮
        self.startcollectbtn = tk.Button(self.basic_frame, text="开始收集", bg="green", command=self.startCollect)

        # 取消收集
        self.cancelcollectbtn = tk.Button(self.basic_frame, text="取消", bg="red", command=self.cancelCollect)
        #隐藏
        self.startcollectbtn.place_forget()
        self.cancelcollectbtn.place_forget()
    def startCollect(self):
        raise Exception
    def cancelCollect(self):
        # 重置取消按钮状态
        self.document_cancel = 0
        #隐藏公有元素
        self.hide_public_elements((self.tuling_cancel,))
        # 隐藏私有元素
        self.cancelcollectbtn.place_forget()
        self.startcollectbtn.place_forget()
        # 重置功能按钮状态
        self.resetStatus()
        # 交回添加删除归属权
        if self.status == 2:
            self.status = 0


    def documents(self):
        self.status = 2
        self.document_cancel = 1
        self.chats_listbox.place(relx=0.45, rely=0.55, relheight=0.3, relwidth=0.3)
        self.chat_scrollbar.pack(side="right", fill="y")
        self.monitoring.place(relx=0.45, rely=0.50)
        self.startcollectbtn.place(x=309, y=150)
        self.cancelcollectbtn.place(x=380, y=150)
        self.dataExchange()
if __name__ == '__main__':
    base = BsDocuMents()
    base.mainloop()