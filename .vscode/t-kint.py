import tkinter as tk


root = tk.Tk()
root.title("CodeBreak")

lbl = tk.Label(root, text="Hello World")
lbl.grid(row=0, column=0)

btn = tk.Button(root, text="Click me")
btn.grid(row=0, column=0)   

root.mainloop()

