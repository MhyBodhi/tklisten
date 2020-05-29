import time
import _tkinter
from interactive.start import Start

if __name__ == '__main__':

    base = Start()
    base.run()
    try:
        base.state()
    except _tkinter.TclError:
        base.q.put(None)
