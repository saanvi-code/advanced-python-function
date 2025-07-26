from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
root=Tk()
root.geometry("500x500")
root.title("text editor")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
text_area=Text(root)
text_area.grid(row=0,column=0,sticky="nsew")
def open_file():
    file_path=askopenfilename()
    if file_path:
        with open(file_path,"r") as file:
            text=file.read()
            text_area.delete(1.0,END)
            text_area.insert(END,text)

def save_file():
    file_path=asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path,"w") as file:
         file.write(text_area.get(1.0,END))
menu_bar=Menu(root)
file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save",command=save_file)
file_menu.add_command(label="exit",command=root.quit)
menu_bar.add_cascade(label="file",menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()







