def analyze_file(file_path):
    word_count = 0
    vowel_count = 0
    blank_space_count = 0
    lowercase_count = 0
    uppercase_count = 0
    
    vowels = "aeiouAEIOU"
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            word_count += len(words)
            
            for char in line:
                if char.isspace():
                    blank_space_count += 1
                elif char.islower():
                    lowercase_count += 1
                elif char.isupper():
                    uppercase_count += 1
                if char in vowels:
                    vowel_count += 1
    
    print("Number of words:", word_count)
    print("Number of vowels:", vowel_count)
    print("Number of blank spaces:", blank_space_count)
    print("Number of lowercase letters:", lowercase_count)
    print("Number of uppercase letters:", uppercase_count)

file_path = "file1.txt"

analyze_file(file_path)
