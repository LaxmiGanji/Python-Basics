def find_most_common_word(file_path):
    word_count = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = word.lower()  
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    
    if word_count:
        most_common_word = max(word_count, key=word_count.get)
        most_common_count = word_count[most_common_word]
        
        print("Most common word:", most_common_word)
        print("Number of occurrences:", most_common_count)
    else:
        print("No words found in the file.")

file_path = "sample.txt"

find_most_common_word(file_path)
