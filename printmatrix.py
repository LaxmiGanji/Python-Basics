rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Enter the value for row {} and column {}: ".format(i+1, j+1)))
        row.append(value)
    matrix.append(row)
for row in matrix:
    print(row)
    
