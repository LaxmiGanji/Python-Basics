import tkinter as tk

class Rectangle:
    #new instance
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def draw_rectangle(canvas, rectangle):
    canvas.create_rectangle(rectangle.x1, rectangle.y1, rectangle.x2, rectangle.y2, outline="black")

root = tk.Tk()
root.title("Rectangle Drawer")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

rect = Rectangle(50, 50, 200, 150)

draw_rectangle(canvas, rect)

root.mainloop()
