import tkinter as tk
def custom_warning():
    warning_window=tk.Toplevel(root)
    warning_window.title("Custom sized messagebox")
    warning_window.geometry("400x200")
    label=tk.Label(warning_window,text="*virus found*",fg="red",font=("italic",20))
    label.pack(pady=20)
    ok_button=tk.Button(warning_window,text="ok",command=warning_window.destroy)
    ok_button.pack()
root=tk.Tk()
root.title("Custom warning")
root.geometry("700x700")
scan_button=tk.Button(root,text="scan for virus",command=custom_warning)
scan_button.pack(pady=40)
root.mainloop()


