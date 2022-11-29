import tkinter as tk
import tkinter.messagebox as tkm

#連続してもいい文字
consecutive_ok = ["(",")"]
for i in range(10):
    consecutive_ok.append(str(i))

#このままevalにつっこむとエラーか地学処理をしそうなので変換する文字
tran = {"x":"*","÷":"/","^":"**"}


def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        que = entry.get()
        for olds,news in tran.items():
            que = que.replace(olds,news)
        try:
            answer = eval(que)
            entry.delete(0,tk.END)
            entry.insert(tk.END,answer)
        except: 
            #0割り等のエラー時に対応
            tkm.showerror(txt,"エラーが発生しました")
    elif txt=="C":
        entry.delete(0,tk.END)
    elif txt == "back":
        siz = len(entry.get())
        entry.delete(max(siz-1,0),tk.END)
    elif txt == "1/x":
        que = entry.get()
        if len(que)>0:
            entry.delete(0,tk.END)
            que = "1/("+que+")"
            entry.insert(tk.END,que)
    #未実装リストに入ってたら表示
    elif txt in ["√"]:
        tkm.showwarning("なんてこったい","まだ実装されていません！")
    #float型になった時にintに強制的に戻すボタン
    elif txt =="int":
        try:
            #floatにしてintにしてstringに直す(まずい)
            que = str(int(float((entry.get()))))
            entry.delete(0,tk.END)
            entry.insert(tk.END,que)
        except:
            pass
    #連続してもいい文字かを判定
    elif txt in consecutive_ok:
        #連続してもいい文字なのでそのまま入れる
        entry.insert(tk.END,txt)
    else:
        #連続したらまずいので最後の文字を取得して
        #それも連続してはいけなかったら追加しない
        #マイナスのみ最初についてもいい
        que = entry.get()
        if len(que)==0 and txt=="-":
            entry.insert(tk.END,txt)
        elif len(que)>0 and que[-1] in consecutive_ok:
            entry.insert(tk.END,txt)
    #tkm.showinfo(txt,f"{txt}が押されました")

#ボタンを追加する関数
def make_button(s):
    global r,c
    siz = 1
    # "="だけ横に長くする
    if s == "=":
       siz = 2 
    button = tk.Button(root,text=s,font=("",30),width=4*siz,height=2)
    button.bind("<1>",button_click)
    button.grid(row=r,column=c,columnspan=siz)
    c += 1
    if c%6==0:
        r += 1
        c = 1

root = tk.Tk()
root.title("Calc")
root.geometry("500x600")


r = 1
c = 1

entry = tk.Entry(root,justify="right",width=17,font=("",40))
entry.grid(row=r,column=c,columnspan=6)

r += 1

#このレイアウトになるようにキーを配置
key_mat = [
        ["^","(",")","÷","back"],
        ["7","8","9","x","1/x"],
        ["4","5","6","-","√"],
        ["1","2","3","+","int"],
        ["0",".","C","="] 
       ]

for key_vec in key_mat:
    for key in key_vec:
        make_button(key)

root.mainloop()