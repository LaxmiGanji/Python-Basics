from tkinter import *

class Canvas:
    def __init__(self, master):
        self.canvas = Canvas(master, width=500, height=500)
        self.canvas.pack()

    def draw_point(self, point):
        x = point.x
        y = point.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

root = Tk()
canvas = Canvas(root)
point = Point(50, 50)
canvas.draw_point(point)
root.mainloop()
