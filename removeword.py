string = "this is a sample string"
word = "sample"
new_string = ' '.join([w for w in string.split() if w!=word ])
print(new_string)
