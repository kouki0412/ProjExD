import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy,mx,my
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    cx = mx*100+50
    cy = my*100+50
    canvas.coords("player",cx,cy)
    root.after(100,main_proc)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500,height=900,bg="black")
    images = tk.PhotoImage(file="fig/0.png")
    mx = 1; my = 1
    cx = mx*100+50; cy = my*150+50
    mp = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,mp)
    canvas.create_image(cx,cy,image=images,tags="player")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    canvas.pack()
    root.mainloop()
