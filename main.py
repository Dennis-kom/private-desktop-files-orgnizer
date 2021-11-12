# ------------- IMPORTS ---------------

import tkinter as tk
from tkinter import *
import functions as fn
from tkinter import messagebox as msg

# --------- GLOBAL CONSTANTS ----------
main_title = "Desktop files Organizer"
main_win_dim = "300x300"


def test():
    print("button click preformed")

def oganize_run():
    fn.create_folers()
    fn.orgnize_execute([chvar1, chvar2, chvar3, chvar4, chvar5, chvar6, chvar7, chvar8])
    msg.showinfo("Complete", "Desktop Organizing Completed!")


top = tk.Tk()
# ---------  WINDOW PARAMETERS ---------
top.title(main_title)
top.geometry(main_win_dim)

# ----------- WIDGETS -------------------

# ----------- WIDGETS : labels ----------

l1 = tk.Frame(top).grid(row=0, column=0)
l2 = tk.Frame(top).grid(row=10, column=0)
# ----------- WIDGETS : check buttons ---
# ----------- checkbox variables --------
chvar1 = IntVar() # docx
chvar2 = IntVar() # pptx
chvar3 = IntVar() # xlsx
chvar4 = IntVar() # pdf
chvar5 = IntVar() # txt
chvar6 = IntVar() # png
chvar7 = IntVar() # jpeg
chvar8 = IntVar() # zip
chvar9 = IntVar() # select all

# ------- checkbuttons area dimentions ---
chb_h = 1
chb_w = 3
# -----------check box ------------------

c1 = tk.Checkbutton(l1, text='docx', variable=chvar1, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=1, column=1,sticky=E)
c2 = tk.Checkbutton(l1, text='pptx', variable=chvar2, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=2, column=1,sticky=E)
c3 = tk.Checkbutton(l1, text='xlsx', variable=chvar3, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=3, column=1,sticky=E)
c4 = tk.Checkbutton(l1, text='pdf', variable=chvar4, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=4, column=1,sticky=E)
c5 = tk.Checkbutton(l1, text='txt', variable=chvar5, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=5, column=1,sticky=E)
c6 = tk.Checkbutton(l1, text='png', variable=chvar6, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=6, column=1,sticky=E)
c7 = tk.Checkbutton(l1, text='jpeg', variable=chvar7, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=7, column=1,sticky=E)
c8 = tk.Checkbutton(l1, text='zip', variable=chvar8, onvalue=1, offvalue=0, height=chb_h, width=chb_w).grid(row=8, column=1,sticky=E)
c9 = tk.Checkbutton(l1, text='select all', variable=chvar9, onvalue=1, offvalue=0, height=chb_h, width=chb_w+10).grid(row=1, column=15,sticky=E)

# ----------- WIDGETS : click buttons ---
organize = tk.Button(l2, text="organize", command=oganize_run).grid(row=100, column=0)


top.mainloop()




