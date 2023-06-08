def palindrome(str1):
  for i in range(0,int(len(str1)/2)):
    if str1[i]!=str1[len(str1)-i-1]:
      return false
   return true
str2=input("enter any string: ")
print(palindrome(str2))
