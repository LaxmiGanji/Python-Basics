n = int(input("enter the limit: "))
f1 = 0
f2 = 1
sum = 0
flag = 1
print("fibonacci series is: ", end = " ")
while (flag<=n):
  flag+=1
  print(sum, end " " )
  f1 = f2
  f2 = sum
  sum =f1 + f2
