import random

def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = [[1 for i in range(tate)] for j in range(yoko)]  #大きさがtate*yokoの「1」の2次元リスト
    for maze_yoko in range(1, len(maze_lst)-1): #壁ではない部分を0にする
        for cell in range(1, len(maze_lst[0])-1):
            maze_lst[maze_yoko][cell] = 0
    for y in range(2, tate-2, 2): #迷路を作る
        for x in range(2, yoko-2, 2):
            maze_lst[x][y] = 1
            if x > 2:
                rnd = random.randint(0, 2)
            else:
                rnd = random.randint(0, 3)
            maze_lst[x+YP[rnd]][y+XP[rnd]] = 1
    return maze_lst

def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for x in range(len(maze_lst)):
        for y in range(len(maze_lst[x])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, fill=color[maze_lst[x][y]])

#2次元リストを渡すとCUIで迷路を表示
def print_maze(maze_lst):
    maze_lst = [list(x) for x in zip(*maze_lst)] #転置
    for i in maze_lst:
        for j in i:
            if j == 1:
                j = "■"
            else:
                j = "□"
            print(j,end="")
        print()

#maze_makerテスト用
if __name__ == "__main__":
    maze = make_maze(15,9)
    print_maze(maze)