import tkinter as tk
import maze_maker
import random
import queue
import copy

#幅優先探索の時とかにつかう変数。便利。
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

#自動と手動を切り替える関数
def mode_change():
    global jid, mode
    if key=="s" and mode!=0:
        mode = 0
        solve()
    elif key=="m" and mode !=1:
        mode = 1
        main_proc()
    root.after(100,mode_change)

#今いる位置からゴールまで自動的に動いてくれる機能
def solve():
    global mx,my,jid,answer
    jid = None
    que = queue.Queue()
    x = mx; y = my
    seen = copy.deepcopy(mp)
    #幅優先探索でゴールまでの経路を探索
    seen[x][y] = 2
    que.put((mx,my,2))
    while(not que.empty()):
        x, y , cnt = que.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if seen[nx][ny]==0:
                que.put((nx,ny,cnt+1))
                seen[nx][ny] = cnt + 1
    x = gx; y = gy 

    #探索結果から経路復元
    answer = []
    answer.append((gx,gy))
    while(x!=mx or y!=my):
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if seen[x][y]-1==seen[nx][ny]:
                answer.append((nx,ny))
                x = nx
                y = ny
    reversed(answer)
    solve_move()

#こうかとんを実際に動かす関数(動かし終わったらmain_procに戻る)
def solve_move():
    global mx,my,cx,cy,answer,jid
    if len(answer)==0:
        mode = 1
        main_proc()
    else:
        mx,my = answer.pop()
        cx = mx*100+50
        cy = my*100+50
        canvas.coords("player",cx,cy)
        root.after(100,solve_move)



def main_proc():
    global cx,cy,mx,my,jid
    if key == "Up" and mp[mx][my-1]==0:
        my -= 1
    if key == "Down" and mp[mx][my+1]==0:
        my += 1
    if key == "Left" and mp[mx-1][my]==0:
        mx -= 1
    if key == "Right" and mp[mx+1][my]==0:
        mx += 1
    cx = mx*100+50
    cy = my*100+50
    canvas.coords("player",cx,cy)
    jid = root.after(100,main_proc)

#スタートを動けるところからランダムに選ぶ。かべのなかにいる。にはならない。
#ゴールは幅優先探索でスタートから最も遠いところに選ばれる

def make_st_and_gl():
    global mx,my,gx,gy
    indexs = []
    for i,vec in enumerate(mp):
        for j,val in enumerate(vec):
            if val == 0:
                indexs.append((i,j))
    mx,my = random.choice(indexs)
    q = queue.Queue()
    x = mx; y = my
    seen = copy.deepcopy(mp)
    q.put((mx,my))
    while(not q.empty()):
        x, y = q.get()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if seen[nx][ny]==0:
                q.put((nx,ny))
                seen[nx][ny] = 1
    #ここめっちゃ怪しいです。
    #幅優先探索なので最後に更新した場所が一番遠いはず
        gx = x; gy = y
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500,height=900,bg="black")
    images = tk.PhotoImage(file="fig/0.png")
    mx = 1; my = 1
    cx = mx*100+50; cy = my*150+50
    # ゴールまでの経路を入れる変数
    answer = []
    # プレイヤーが操作しているか自動なのか(1は手動、0は自動)
    mode = 1
    # ゴールがある座標
    gx = 0; gy = 0
    mp = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,mp)
    canvas.create_image(cx,cy,image=images,tags="player")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    #スタートとゴールを生成する関数
    make_st_and_gl()
    goal = tk.PhotoImage(file="fig/goal.png")
    canvas.create_image(gx*100+50,gy*100+50,image=goal,tags="goal")
    #モードを管理する関数を動かす
    mode_change()
    main_proc()
    canvas.pack()
    root.mainloop()
