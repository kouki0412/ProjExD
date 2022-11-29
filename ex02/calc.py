import tkinter as tk
import tkinter.messagebox as tkm

consecutive_ok = ["(",")"]
for i in range(10):
    consecutive_ok.append(str(i))

tran = {"x":"*","÷":"/","^":"**"}


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        que = entry.get()
        for olds,news in tran.items():
            que = que.replace(olds,news)
        entry.delete(0,tk.END)
        entry.insert(tk.END,eval(que))
    elif txt=="C":
        entry.delete(0,tk.END)
    elif txt in consecutive_ok:
        entry.insert(tk.END,txt)
    else:
        que = entry.get()
        if que[-1] in consecutive_ok:
            entry.insert(tk.END,txt)
    #tkm.showinfo(txt,f"{txt}が押されました")

def make_button(s):
    global r,c
    button = tk.Button(root,text=s,font=("",30),width=4,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c)
    c += 1
    if c%5==0:
        r += 1
        c = 1

root = tk.Tk()
root.title("Calc")
root.geometry("400x600")


r = 1
c = 1

entry = tk.Entry(root,justify="right",width=15,font=("",40))
entry.grid(row=r,column=c,columnspan=4)

r += 1

#このレイアウトになるようにキーを配置
key_mat = [
        ["^","(",")","÷"],
        ["7","8","9","x"],
        ["4","5","6","-"],
        ["1","2","3","+"],
        ["0",".","C","="] 
       ]

for key_vec in key_mat:
    for key in key_vec:
        make_button(key)

root.mainloop()