import tkinter as t
from tkinter import messagebox

def scan_virus():
    messagebox.showwarning("virus found")
root=t.Tk()
root.title("Virus scanner")
root.geometry("500x500")
but=t.Button(root,text="scan for virus",command=scan_virus)
but.place(x=200,y=250)
t.mainloop()