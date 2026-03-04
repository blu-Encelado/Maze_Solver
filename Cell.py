from Window import *

class Cell:
    def __init__(self, window=Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1=-1
        self.__x2=-1
        self.__y1=-1
        self.__y2=-1
        self.__win=window
    
    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")