import os
import time
import _tkinter
from interactive.start import Start
from bak.select import Bak

if __name__ == '__main__':
    base = Start()
    base.run()
    try:
        base.state()
    except _tkinter.TclError:
        base.q.put(None)
        time.sleep(0.1)
        try:
            os.remove(Bak.file_img_path)
            os.remove(Bak.file_mp3_path)
            os.remove(Bak.erweima_png_path)
        except Exception as e:
            print("错误",e)
