with open ("file1.txt") as fp:
  data = fp.read()
inputword = input("enter a word to check in the file: ")
for fileword in data.split():
  if (fileword == inputword):
    print(fileword)
