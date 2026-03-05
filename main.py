from Window import *
from Point_Line import *
from src.config import *
from Maze_from_Cells import *

def main():
    print(Title, "start")
    win = Window(Width, Height, Title)
    
    maze = Maze(25,25,10,10,100,100,win)

    win.wait_for_close()


if __name__ == "__main__":
    main()