import time
import _tkinter
from interactive.start import Start

if __name__ == '__main__':

    base = Start()
    base.run()
    while True:
        try:
            base.q.put(1)
            base.state()
        except _tkinter.TclError:
            base.q.put(None)
            time.sleep(0.1)
            break