from tkinter import Tk, BOTH, Canvas
from Point_Line import*

class Window:
    def __init__(self, width, height, title):
        self.__root = Tk()
        self.__root.title(title)
        self.canvas = Canvas(self.__root,bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close())
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
    
    def close(self):
        self.is_running = False
    
    def draw_line(self, line:Line, fill_color):
        line.draw(self.canvas, fill_color)