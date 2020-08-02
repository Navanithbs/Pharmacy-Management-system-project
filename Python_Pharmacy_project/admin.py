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

import admin_support
from tkinter import messagebox as mb
import os.path

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1 (root)
    admin_support.init(root, top)
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
    admin_support.init(w, top, *args, **kwargs)
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
        font10 = "-family {DejaVu Sans} -size 20 -weight bold "  \
            "-underline 1"
        font12 = "-family {DejaVu Sans} -size 11 -weight bold"

        top.geometry("605x450+339+168")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("Admin Page")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.15, rely=0.178, height=91, width=394)
        self.Label1.configure(cursor="fleur")
        photo_location = os.path.join(prog_location,"/home/navanith/Documents/Python_Pharmacy_project/drugs.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.068, rely=0.067, height=41, width=523)
        self.Label2.configure(font=font10)
        self.Label2.configure(text='''Pharmacy Management System''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.083, rely=0.489, height=21, width=119)
        self.Label3.configure(font=font12)
        self.Label3.configure(text='''Tablet Name :''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.083, rely=0.556, height=21, width=110)
        self.Label4.configure(font=font12)
        self.Label4.configure(text='''Dosage :''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.017, rely=0.622, height=21, width=180)
        self.Label5.configure(cursor="fleur")
        self.Label5.configure(font=font12)
        self.Label5.configure(text='''Manufacturing Date :''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.05, rely=0.689, height=21, width=161)
        self.Label6.configure(font=font12)
        self.Label6.configure(text='''Expiry Date :''')

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.068, rely=0.756, height=21, width=130)
        self.Label7.configure(font=font12)
        self.Label7.configure(text='''Price :''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.35, rely=0.489,height=23, relwidth=0.506)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.35, rely=0.556,height=23, relwidth=0.506)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.35, rely=0.622,height=23, relwidth=0.506)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#020202")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.35, rely=0.689,height=23, relwidth=0.506)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.347, rely=0.756,height=23, relwidth=0.506)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.4, rely=0.867, height=31, width=89)
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(font=font12)
        self.Button1.configure(text='''Add''')
        from os.path import join as pjoin
        def writefiles(self):
                if self.Entry1.get()=="":
                        mb.showinfo(title="Error",message="Enter valid name")
                else:
                        first=self.Entry1.get()+".txt"
                        path_to_file=pjoin("/","home","navanith","Documents","Python_Pharmacy_project","files",first)
                        with open(path_to_file,"w") as wr:
                                wr.write("Tablet name :"+str(self.Entry1.get()+"\n")+"Dosage :"+str(self.Entry2.get()+"\n")+
                                "Manufacturing Date :"+str(self.Entry3.get()+"\n")+"Expiry :"+str(self.Entry4.get()+"\n")+
                                "Price :"+str(self.Entry5.get()+"\n\n"))
                                mb.showinfo(title="Confirmation",message="Tablet Entered Successful")
                        wr.close()
                        self.Entry1.delete(0,"end")
                        self.Entry2.delete(0,"end")
                        self.Entry3.delete(0,"end")
                        self.Entry4.delete(0,"end")
                        self.Entry5.delete(0,"end")
        self.Button1.configure(command=lambda: writefiles(self))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.628, rely=0.867, height=31, width=88)
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(font=font12)
        self.Button2.configure(text='''Delete''')
        def delBooking(self):
                first=self.Entry1.get()+".txt"
                flist=os.listdir('/home/navanith/Documents/Python_Pharmacy_project/files')
                if self.Entry1.get() and self.Entry2.get()=="":
                        mb.showinfo(title="Error",message="Enter valid details..!!!!")
                elif first not in flist:
                        root.destroy()
                        mb.showinfo(title="Error",message="Tablet not in list!!!")
                else:
                        os.remove('/home/navanith/Documents/Python_Pharmacy_project/files/'+first)
                        root.destroy()
                        mb.showinfo(title="confirmation",message="Tablet Removed Successfully...!!!")
        self.Button2.configure(command=lambda: delBooking(self))

if __name__ == '__main__':
    vp_start_gui()





