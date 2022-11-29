import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("Calc")
root.geometry("300x500")

button = dict()

for i in range(10):
    button[str(i)] = tk.Button(root,text=str(i),font=("",30),width=4,height=2)
    button[str(i)].grid(row =(9-i)//3+1,column=(9-i)%3+1)

root.mainloop()