import tkinter as tk

class Rectangle:
    def __init__(self, canvas, x1, y1, x2, y2, color="black"):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.draw()

    def draw(self):
        self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", fill=self.color)

root = tk.Tk()
root.title("Rectangle Drawer")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
rect1 = Rectangle(canvas, 50, 50, 200, 150, color="blue")
rect2 = Rectangle(canvas, 100, 100, 250, 250)

root.mainloop()
