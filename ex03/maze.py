import tkinter as tk

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(width=1500,height=900,bg="black")
    images = tk.PhotoImage(file="fig/0.png")

    cx = 300; cy = 400
    canvas.create_image(cx,cy,image=images)
    key = ""
    root.bind("<KeyRelease>",key_down)
    canvas.pack()
    root.mainloop()
