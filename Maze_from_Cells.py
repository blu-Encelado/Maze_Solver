import random

from Window import *
import time

class Cell:
    def __init__(self, window:Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win=window
        self.visited = False
        

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color)
    
class Maze:
    def __init__(self,x1,y1,num_rows,num_cols,cell_size_x, cell_size_y, win:Window=None, seed=None):
        if seed is not None:
            random.seed(seed)
        self.x1=x1
        self.y1=y1
        self.__num_rows=num_rows
        self.__num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win=win
        self.__cells=[]
        self.__create_cells()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            row=[]
            for j in range(self.__num_rows):
                row.append(Cell(self.win))
            self.__cells.append(row)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)        

    def get_single_cell(self, i, l):
        return self.__cells[i][l]

    def get_whole_cells(self):
        return self.__cells

    def __draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate(0.01)

    def __animate(self, n):
        if self.win == None:
            return
        
        self.win.redraw()
        time.sleep(n)
    
    def _break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[0][0].has_bottom_wall = False
        self.__draw_cell(0,0)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            current = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                current.append((i - 1, j))
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                current.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                current.append((i, j - 1))
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                current.append((i, j + 1))
            
            if len(current) == 0:
                self.__draw_cell(i,j)
                return

            random_index = random.randrange(len(current))
            next_cell=current[random_index]

            if next_cell[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i+1][j].has_left_wall = False

            if next_cell[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i-1][j].has_right_wall = False

            if next_cell[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j+1].has_top_wall = False

            if next_cell[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j-1].has_bottom_wall = False
            
            self.__break_walls_r(next_cell[0], next_cell[1])
    
    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited=False

    def _solve_r(self, i, j):
        self.__animate(0.1)
        
        self.__cells[i][j].visited = True

        if i== self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        
        if (i > 0 
            and not self.__cells[i][j].has_left_wall 
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i - 1][j], True)

        if (i < self.__num_cols - 1 
            and not self.__cells[i][j].has_right_wall 
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i + 1][j], True)

        if (j > 0 
            and not self.__cells[i][j].has_top_wall 
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j - 1], True)


        if (j < self.__num_rows 
            and not self.__cells[i][j].has_bottom_wall 
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self.__cells[i][j].draw_move(self.__cells[i][j + 1], True)

        
        

        return False  

    def solve(self):
        return self._solve_r(0, 0)