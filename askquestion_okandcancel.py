import tkinter as T
from tkinter import messagebox
def questionaire():
    messagebox.askquestion("Do you like oranges")

def freemoney():
    messagebox.askokcancel("Do you want FREE MONEY? Just click ok")
window=T.Tk()
window.title("Ask a question, win an answer")
window.geometry("500x500")
ques_btn=T.Button(window,text="Recieve a question",command=questionaire)
ques_btn.place(x=50,y=50)
freemon=T.Button(window,text="CLICK for a spam",command=freemoney)
freemon.place(x=250,y=50)
window.mainloop()