import tkinter as tk

import constants.main_window_constants as const
from graphics.gui.main_gui import MainGUI


def on_closing():
    main_gui.on_closing()
    exit_app()


def exit_app():
    root.destroy()


root = tk.Tk()
main_gui = MainGUI(root, exit_app)


root.title(const.MW_TITLE)
root.protocol("WM_DELETE_WINDOW", on_closing)

main_gui.run()

RWidth = root.winfo_screenwidth()
RHeight = root.winfo_screenheight()
root.geometry('%dx%d' % (RWidth, RHeight))

root.update()

root.minsize(1700, 900)
root.attributes('-fullscreen', True)
# root.state('zoomed')

# root.minsize(root.winfo_width(), root.winfo_height())
# root.maxsize(root.winfo_width(), root.winfo_height())
# root.resizable(0, 0)

root.mainloop()
