from bases.bsdocuments import BsDocuMents,msg
import tkinter as tk
class BsService(BsDocuMents):
    def __init__(self):
        super().__init__()
        self.text_service_info = tk.StringVar(self)
        self.label_showinfo = tk.Label(self.basic_frame,textvariable=self.text_service_info, fg="blue", bg="#8A2BE2", font=("黑体", 10))

        #隐藏
        self.label_showinfo.place_forget()
        #用户点击指针。重点说明：此指针非彼指针，万一不小心误导了小白呢
        self.user_click = 0
    def service(self):
        self.service_cancel = 1
        if self.user_click >=3:
            self.text_service_info.set("请耐心等待...")
        else:
            self.text_service_info.set("暂时不支持该功能")
        self.label_showinfo.place(x=309,y=200)
        self.user_click += 1
if __name__ == '__main__':
    # base = BsService()
    # base.mainloop()
    if False  in [i==0 for i in (1,3)]:
        print("ok")
