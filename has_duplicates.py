def has_duplicates(templist):
  seen = set()
  for i in templist:
      if i in seen:
          return True
      seen.add(i)
  return False
list1=[5,4,4,"ten","ten"]
print("list1 has duplicates: ",has_duplicates(list1))
