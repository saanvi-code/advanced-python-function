from tkinter import *
from datetime import date
window=Tk()
window.title('Getting started with widgets')
window.geometry('500x500')
Label(window,text="Hello",fg="white",bg="black",width=500).pack()
Label(window,text="Enter your name:",bg="yellow").pack()
name_entry=Entry(window)
name_entry.pack()
Text_box=Text(window,height=10)
Text_box.pack()
def display():
    name=name_entry.get()
    message=f"hello {name} \n Welcome to the Application \n Today's date is {date.today()}"
    Text_box.insert(END,message)
Button(window,text="start",command=display,bg="white",fg="blue").pack()

window.mainloop()

