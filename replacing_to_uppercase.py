def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = []
    
    for word in words:
        capitalized_word = word[0].upper() + word[1:].lower()
        capitalized_words.append(capitalized_word)
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence
sentence = "replacing the first letter to uppercase"
capitalized_sentence = capitalize_first_letter(sentence)
print(capitalized_sentence)
