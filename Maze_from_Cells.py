from Window import *
import time

class Cell:
    def __init__(self, window:Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1=-1
        self.__x2=-1
        self.__y1=-1
        self.__y2=-1
        self.__win=window
        self.c_x = 0 
        self.c_y = 0

    def draw(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.c_x, self.c_y = self.get_center()

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"

        self.__win.draw_line(Line(Point(self.c_x, self.c_y), Point(to_cell.c_x, to_cell.c_y)), color)
    
    def get_center(cell):
        center_x = (abs(cell.__x2 - cell.__x1) // 2) + cell.__x1
        center_y = (abs(cell.__y2 - cell.__y1) // 2) + cell.__y1
        
        return center_x, center_y
    
class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x, cell_size_y, win:Window=None,):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self.__cells=[]
        self.__create_cells()

    def __create_cells(self):
        grid=[]
        for i in range(self.num_cols):
            row=[]
            for j in range(self.num_rows):
                new_cell = Cell(self.win)
                row.append(new_cell)
                self.__draw_cell(i,j)
            grid.append(row)
        self.__cells=grid

        self.__animate()

        

    def __draw_cell(self, i, j):
        x1 = i * self.cell_size_x + self.x1
        y1 = j * self.cell_size_y + self.y1
        x2 = x1 + self.cell_size_x 
        y2 = y1 + self.cell_size_y 

        if self.win == None:
            return
        Cell(self.win).draw(x1,x2,y1,y2)

    def __animate(self):
        if self.win == None:
            return
        while True:
            self.win.redraw()
            time.sleep(0.5)