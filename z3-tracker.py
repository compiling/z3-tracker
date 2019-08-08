import sys

if sys.version_info.major < 3:
    errortext = (
        'You are using Python {0:d}.{1:d}. z3-tracker requires at least Python '
        '{2:d}.{3:d}.'.format(
                sys.version_info.major, sys.version_info.minor, 3, 6))
    try:
        import Tkinter
        import tkMessageBox
        tkMessageBox.showerror('Wrong Python version', errortext)
    except:
        print (errortext)
    sys.exit()

import z3tracker.main
z3tracker.main.main()
