n = int(input("Enter the size of the square matrices: "))

matrix1 = []
matrix2 = []

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

result = []
for i in range(n):
    row = []
    for j in range(n):
        value = 0
        for k in range(n):
            value += matrix1[i][k] * matrix2[k][j]
        row.append(value)
    result.append(row)

print("The product of the matrices is:")
for row in result:
    print(row)
