from tkinter import *

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class Canvas:
    def __init__(self, master):
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

    def draw_circle(self, circle):
        x = circle.x
        y = circle.y
        r = circle.radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black")

root = Tk()
canvas = Canvas(root)
circle1 = Circle(50, 50, 20)
circle2 = Circle(100, 100, 30)
canvas.draw_circle(circle1)
canvas.draw_circle(circle2)
root.mainloop()
