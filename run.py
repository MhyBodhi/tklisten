import os
import time
import _tkinter
import multiprocessing
from interactive.start import Start
from bak.select import Bak

if __name__ == '__main__':
    multiprocessing.freeze_support()
    base = Start()
    base.run()
    try:
        base.state()
    except _tkinter.TclError:
        base.q.put(None)
        time.sleep(0.1)
        try:
            os.remove(Bak.file_mp3_path)
            os.remove(Bak.erweima_png_path)
            try:
                for file in os.listdir("bg"):os.remove("bg/"+file)
                os.removedirs("bg")
            except:
                raise
        except Exception as e:
            print("错误", e)

