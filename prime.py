first_value = int(input("enter the first value: "))
last_value = int(input("enter the last value: "))
print("the prime numbers are: ")
for num in range (first_value, last_value + 1):
  if ( num > 1 ):
    for i in range (2, num):
      if (num % 1) ==0:
        break
    else:
      print(num)
