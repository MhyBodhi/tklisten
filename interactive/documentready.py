from chatready import ChatReady
import tkinter as tk
class DocumentReady(ChatReady):
    def __init__(self):
        super().__init__()
        #收集文件初始化
        self.document_ready = tk.Label(self.basic_frame, text="文件收集准备就绪...", fg="black", bg="#8A2BE2", font=("黑体", 12))
        #取消准备就绪
        self.cancel_document_start = tk.Button(self.basic_frame, text="取消准备", fg="black", bg="red", font=("黑体", 10),command=self.cancelDocument)

        #隐藏
        self.document_ready.place_forget()
        self.cancel_document_start.place_forget()
    def documents(self):
        super().documents()
        self.label_api_error.place_forget()
    def startCollect(self):
        if self.chats_listbox.size()==0:
            self.text_api_error.set("监控对象列表不能为空")
            self.label_api_error.place(x=280, y=130, width=150, height=20)
            return
        self.document_ready_status = 1

        self.documentsbtn.place_forget()
        self.startcollectbtn.place_forget()
        self.cancelcollectbtn.place_forget()

        self.document_ready.place(x=215, y=150)
        self.cancel_document_start.place(x=380, y=150)
        self.startbtu.configure(bg="green", relief="raised", stat="active")

        if self.tuling_ready_status == 1 and self.document_ready_status == 1:
            self.chats_listbox.place_forget()
            self.monitoring.place_forget()


    def cancelDocument(self):
        self.document_ready_status = 0

        self.chats_listbox.place(relx=0.45, rely=0.55, relheight=0.3, relwidth=0.3)
        self.monitoring.place(relx=0.45, rely=0.50)
        self.documentsbtn.place(x=215, y=150)
        self.startcollectbtn.place(x=309, y=150)
        self.cancelcollectbtn.place(x=380, y=150)
        self.document_ready.place_forget()
        self.cancel_document_start.place_forget()

        if self.document_ready_status == 1 or self.tuling_ready_status == 1:
            self.startbtu.configure(bg="green", relief="raised", stat="active")
        else:
            self.startbtu.configure(bg="red", relief="sunken", stat="disable")

if __name__ == '__main__':
    base = DocumentReady()
    base.mainloop()
