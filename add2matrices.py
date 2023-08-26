n = int(input("Enter the size of the square matrix: "))
matrix1 = []
matrix2 = []
result = []

print("Enter the values for the first matrix:")
for i in range(n):
    row = []
    for j in range(n):
        value = int(input("Enter the value for row {} and column {}: ".format(i+1, j+1)))
        row.append(value)
    matrix1.append(row)

print("Enter the values for the second matrix:")
for i in range(n):
    row = []
    for j in range(n):
        value = int(input("Enter the value for row {} and column {}: ".format(i+1, j+1)))
        row.append(value)
    matrix2.append(row)

for i in range(n):
    row = []
    for j in range(n):
        value = matrix1[i][j] + matrix2[i][j]
        row.append(value)
    result.append(row)

print("The sum of the matrices is:")
for row in result:
    print(row)
