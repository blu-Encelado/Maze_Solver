from Window import *
from Point_Line import *
from src.config import *
from Cell import *

def main():
    print(Title, "start")
    win = Window(Width, Height, Title)
    
    cell = Cell(win)
    cell.draw(50, 200, 50, 200)
    cell.draw(25, 150, 25, 150)
    cell.draw(2, 400, 8, 300)


    win.wait_for_close()


if __name__ == "__main__":
    main()