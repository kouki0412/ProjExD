import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}が押されました")

def make_button(s):
    global r,c
    button = tk.Button(root,text=s,font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if c%4==0:
        r += 1
        c = 1

root = tk.Tk()
root.title("Calc")
root.geometry("300x500")


r = 1
c = 1

entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=r,column=c,columnspan=3)

r += 1

for i in range(9,-1,-1):
    make_button(str(i))
make_button("+")
make_button("=")

root.mainloop()