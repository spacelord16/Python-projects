def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))
print(reverse_string_words("is: name my Hi"))
print(reverse_string_words("Aditya Deshpande"))