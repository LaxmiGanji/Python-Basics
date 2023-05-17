
input_char = input("Enter a character: ")
if input_char.isdigit():
    print("Input is a digit.")
elif input_char.islower():
    print("Input is a lowercase character.")
elif input_char.isupper():
    print("Input is an uppercase character.")
else:
    print("Input is a special character.")

#or

ch = input("enter the character: ")
if(ord(ch)>=65 and ord(ch)<=90):
  print("upper")
 elif(ord(ch)>=97 and ord(ch)<=122):
  print("lower")
 elif(ord(ch)>=48 and ord(ch)<=57):
  print("number")
 else:
  print("symbol")
