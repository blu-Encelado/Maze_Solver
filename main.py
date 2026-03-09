from Window import *
from Point_Line import *
from src.config import *
from Maze_from_Cells import *

def main():
    print(Title, "start")
    win = Window(Width, Height, Title)
    
    m1 = Maze(25,25,25,25,20,20,win,10)

    m1.solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()