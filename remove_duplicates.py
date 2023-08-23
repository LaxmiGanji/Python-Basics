def remove_duplicates(list):
  seen = set()
  new_list = []
  for element in list:
    if element not in seen:
      seen.add(element)
      new_list.append(element)
  return new_list
list1=[1,2,3,4,4,5,5,6,1]
print("the list after removing duplicates: ",remove_duplicates(list1))
