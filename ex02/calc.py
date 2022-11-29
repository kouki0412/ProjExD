import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}が押されました")

root = tk.Tk()
root.title("Calc")
root.geometry("300x500")

entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=1,column=1,columnspan=3)

for i in range(10):
    button = tk.Button(root,text=str(i),font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row =(9-i)//3+2,column=(9-i)%3+1)

root.mainloop()