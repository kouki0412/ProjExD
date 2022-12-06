import tkinter as tk
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy
    if key == "Up":
        cy -= 20
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("player",cx,cy)
    root.after(100,main_proc)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500,height=900,bg="black")
    images = tk.PhotoImage(file="fig/0.png")

    cx = 300; cy = 400
    mp = maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,mp)
    canvas.create_image(cx,cy,image=images,tags="player")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    canvas.pack()
    root.mainloop()
