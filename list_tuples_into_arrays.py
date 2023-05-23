list_data = [1, 2, 3, 4, 5]
array_from_list = [x for x in list_data]
tuple_data = (6, 7, 8, 9, 10)
array_from_tuple = [x for x in tuple_data]
print("List to array: ")
print(array_from_list)
print("\nTuple to array: ")
print(array_from_tuple)

#using functions
def convert_to_array(data):
    if isinstance(data, list):
        return [x for x in data]
    if isinstance(data, tuple):
        return [x for x in data]
    return None
list_data = [1, 2, 3, 4, 5]
tuple_data = (6, 7, 8, 9, 10)
array_from_list = convert_to_array(list_data)
array_from_tuple = convert_to_array(tuple_data)
print("List to array:")
print(array_from_list)
print("\nTuple to array:")
print(array_from_tuple)
