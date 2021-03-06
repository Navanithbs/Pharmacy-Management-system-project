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

import paymentpage_support
from tkinter import messagebox as mb

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    paymentpage_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    paymentpage_support.init(w, top, *args, **kwargs)
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

        top.geometry("590x450+392+191")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Payments")
        top.configure(background="#727272")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.136, rely=0.267, height=51, width=419)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font="-family {DejaVu Sans} -size 16 -weight bold -slant roman -underline 1 -overstrike 0")
        self.Label1.configure(text='''Payments Page''')

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.153, rely=0.444, relheight=0.478
                , relwidth=0.685)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="6")
        self.Frame1.configure(relief="groove")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.05, rely=0.186, height=22, width=137)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(borderwidth="3")
        self.Label2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label2.configure(text='''Card number :''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.05, rely=0.326, height=21, width=144)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label3.configure(text='''Name on card :''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.074, rely=0.465, height=22, width=126)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Label4.configure(text='''Cvv :''')

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.396, rely=0.651, height=39, width=96)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(borderwidth="5")
        self.Button1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Button1.configure(text='''Confirm''')
        def next():
            if self.Entry1.get()=="":
                mb.showinfo(title="Error",message="Enter valid Details..!!!!")
            else:
                mb.showinfo(title="Confirmation",message="Payment Done Successfully!!:)")
                root.destroy()
        self.Button1.configure(command=next)

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.446, rely=0.186,height=23, relwidth=0.411)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(selectforeground="white")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.446, rely=0.326,height=23, relwidth=0.411)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(selectforeground="white")

        self.Entry3 = tk.Entry(self.Frame1)
        self.Entry3.place(relx=0.446, rely=0.465,height=23, relwidth=0.411)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(selectforeground="white")

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.0, rely=0.044, height=61, width=589)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(font="-family {DejaVu Sans} -size 21 -weight bold -slant roman -underline 1 -overstrike 0")
        self.Label5.configure(text='''Pharmacy Management System''')

if __name__ == '__main__':
    vp_start_gui()





