import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import openpage_support
import os.path
from tkinter import messagebox as mb

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    openpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    openpage_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def next(self):
    if self.Entry1.get()=="admin" and self.Entry2.get()=="admin":
        import admin
        root.destroy()
        admin.vp_start_gui()
    elif self.Entry1.get()=="user" and self.Entry2.get()=="user":
        import user
        root.destroy()
        user.vp_start_gui()
    else:
        mb.showinfo(title="error",message="Invaild Username or Password")

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans} -size 11 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Noto Sans Lao} -size 21 -weight bold -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("600x450+370+185")
        top.title("--Login page--")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.017, rely=0.022, height=81, width=579)
        self.Label2.configure(borderwidth="6")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''PHARMACY MANAGEMENT SYSTEM''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.017, rely=0.167, height=81, width=579)
        self.Label5.configure(borderwidth="6")
        self.Label5.configure(font=font9)
        self.Label5.configure(text='''---------------------------------------------''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.167, rely=0.267, height=151, width=349)
        self.Label1.configure(borderwidth="6")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Python_Pharmacy_project/drugs.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.15, rely=0.667, height=26, width=85)
        self.Label3.configure(borderwidth="3")
        self.Label3.configure(font=font10)
        self.Label3.configure(text='''Login Id :''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.133, rely=0.733, height=26, width=100)
        self.Label4.configure(borderwidth="3")
        self.Label4.configure(font=font10)
        self.Label4.configure(text='''Password :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.3, rely=0.667,height=23, relwidth=0.427, bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.3, rely=0.733,height=23, relwidth=0.427, bordermode='ignore')
        self.Entry2.configure(background="white")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(show="*")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.500, rely=0.8, height=38, width=93)
        self.Button1.configure(font="-family {DejaVu Sans} -size 10 -weight bold -slant italic -underline 0 -overstrike 0")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(text='''Login: )''')
        self.Button1.configure(command=lambda: next(self))

if __name__ == '__main__':
    vp_start_gui()





