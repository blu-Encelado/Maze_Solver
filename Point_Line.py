from tkinter import Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.a = point_a 
        self.b = point_b
    
    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, width=2, fill=fill_color)
