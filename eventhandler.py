import tkinter as t
from tkinter import messagebox
def on_button_click():
    messagebox.showinfo("button clicked")
# Only works when key is active, it mustn't be closed.
def on_key_press(event):
    messagebox.showinfo("Key Pressed{event.char}")


window=t.Tk()
window.title("eventhandler")
window.geometry("600x600")
btn=t.Button(window,text="button to be clicked",command=on_button_click)
# padx is horizontal spacing and pady is vertical spacing
btn.pack(pady=20)
window.bind("<Key>",on_key_press)
window.mainloop()