import tkinter as TK
from tkinter import messagebox
window=TK.Tk()
window.title("Login screen")
window.geometry("500x500")
TK.Label(window,text="username").pack()
user_entry=TK.Entry(window,justify="left")
user_entry.pack(pady=5)
TK.Label(window,text="password").pack()
pass_entry=TK.Entry(window,show="*")
pass_entry.pack(pady=5)
def login():
    username=user_entry.get()
    password=pass_entry.get()
    if username=="admin" and password=="1234":
        messagebox.showinfo("Successful login")

    else:
        messagebox.showerror("Invalid")

TK.Button(window,text="login",command=login).pack()
TK.mainloop()
