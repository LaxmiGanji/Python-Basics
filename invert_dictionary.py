def invert_dict(d):
    inverted_dict = {}
    for key, value in d.items():
        inverted_dict.setdefault(value, []).append(key)
    return inverted_dict

d = {}
n = int(input("Enter the number of key-value pairs: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("Original dictionary:", d)
inverted_dict = invert_dict(d)
print("Inverted dictionary:", inverted_dict)
