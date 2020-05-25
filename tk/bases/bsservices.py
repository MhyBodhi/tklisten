from bases.bsdocuments import BsDocuMents
import tkinter as tk
class BsService(BsDocuMents):
    def __init__(self):
        super().__init__()
        self.label_showinfo = tk.Label(self.basic_frame,text="开发中...", fg="blue", bg="#8A2BE2", font=("黑体", 10))

        #隐藏
        self.label_showinfo.place_forget()
    def service(self):
        self.service_cancel = 1
        self.label_showinfo.place(x=309,y=200)

if __name__ == '__main__':
    # base = BsService()
    # base.mainloop()
    if False  in [i==0 for i in (1,3)]:
        print("ok")
