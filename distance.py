import math
x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance between the two points:", distance)
