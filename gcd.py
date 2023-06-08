def gcd_rec(a,b):
  if(b == 0):
    return a
  else:
    return gcd_rec(b,a%b)
x=int(input("enter the first number: "))
y=int(input("enter the second number: "))
num=gcd_rec(x,y)
print("gcd of two number is: ")
print(num)
