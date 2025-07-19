from tkinter import *
window=Tk()
window.title("Numberpad")
window.geometry("320x420")
entry=Entry(window,width=50,font=("arial",24),bd=5,justify="right")
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=20)
def press_num(number):
    current=entry.get()
    entry.delete(0,END)
    entry.insert(END,current+str(number))
def clear():
    entry.delete(0,END)

def add():
    


buttons=[('1',1,0),('2',1,1),('3',1,2),('4',2,0),('5',2,1),('6',2,2),('7',3,0),('8',3,1),('9',3,2),('0',4,1)]
for (text,row,col) in buttons:
    Button(window,text=text,width=10,height=3,command=lambda t=text:press_num(t)).grid(row=row,column=col)
Button(window,text='clear',width=10,height=3,command=clear).grid(row=4,column=0)
Button(window,text='exit',width=10,height=3,command=window.quit).grid(row=4,column=2)
window.mainloop()