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

import user_support
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
    user_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    user_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {DejaVu Sans} -size 19 -weight bold "  \
            "-underline 1"
        font11 = "-family {DejaVu Sans} -size 11 -weight bold"
        font12 = "-family {DejaVu Sans} -size 10 -weight bold"

        top.geometry("600x450+364+181")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("User Page")
        top.configure(background="#727272")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.083, rely=0.067, height=41, width=489)
        self.Label1.configure(font=font10)
        self.Label1.configure(text='''Pharmacy Management System''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.183, rely=0.2, height=141, width=349)
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Python_Pharmacy_project/med (1).png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)
        self.Label2.configure(text='''Label''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.117, rely=0.6, height=31, width=129)
        self.Label3.configure(background="#727272")
        self.Label3.configure(font=font11)
        self.Label3.configure(text='''Tablet Name :''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.117, rely=0.667, height=31, width=129)
        self.Label4.configure(background="#727272")
        self.Label4.configure(font=font11)
        self.Label4.configure(text='''Dosage :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.35, rely=0.6,height=23, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.35, rely=0.689,height=23, relwidth=0.41)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.283, rely=0.822, height=31, width=86)
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(font=font12)
        self.Button1.configure(text='''Search''')
        def search1(self):
                first=self.Entry1.get()+".txt"
                flist=os.listdir('/home/navanith/Documents/Python_Pharmacy_project/files')
                if self.Entry1.get() and self.Entry2.get()=="":
                        mb.showinfo(title="Error",message="Enter valid details..!!!!")
                elif first not in flist:
                        mb.showinfo(title="Error",message="Tablet not found!!!")
                else:
                        mb.showinfo(title="confiration",message="Tablet is in cart!!!")

        self.Button1.configure(command=lambda: search1(self))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.567, rely=0.822, height=31, width=152)
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(font=font12)
        self.Button2.configure(text='''Proceed To Buy''')
        def next():
            if self.Entry1.get()=="":
                    mb.showinfo(title="Error",message="Enter valid details..!!!!")
            else:   
                import paymentpage
                root.destroy()
                paymentpage.vp_start_gui()
        self.Button2.configure(command=next)

if __name__ == '__main__':
    vp_start_gui()





