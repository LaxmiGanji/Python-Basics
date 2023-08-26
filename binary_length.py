def generate_binary_strings(n):
    if n == 0:
        return ['']
    else:
        strings = generate_binary_strings(n-1)
        return [s + '0' for s in strings] + [s + '1' for s in strings]
n = int(input("enter the value: "))
binary_strings = generate_binary_strings(n)
print(binary_strings)
