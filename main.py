from Window import *
from Point_Line import *
from src.config import *

def main():
    print(Title, "start")
    win = Window(Width, Height, Title)
    

    line_a=Line(Point(5,5), Point(400,300))
    line_b=Line(Point(2,20), Point(400,300))
    line_c=Line(Point(1,80), Point(400,300))
    line_d=Line(Point(520,790), Point(400,300))

    win.draw_line(line_a, "black")
    win.draw_line(line_b, "black")
    win.draw_line(line_c, "black")
    win.draw_line(line_d, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()