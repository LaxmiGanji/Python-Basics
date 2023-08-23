def is_sorted(list):
  for i in range(len(list) - 1):
    if list[i] > list[i + 1]:
      return False
  return True
list1=[1,2,3,4,5]
list2=[9,7,8,6,5]
print("list1 is sorted: ",is_sorted(list1))
print("list1 is sorted: ",is_sorted(list2))
