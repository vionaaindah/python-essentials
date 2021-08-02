from collections import Counter
from os import strerror

srcname = input("Enter the source file name: ")

try:
    text = open(srcname, 'rt')
    char = ''
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            char = char + ch
        else:
            continue
    c = Counter(char)
    c = c.most_common()

    for letter, repetitions in c:
        print(letter, "->", repetitions)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
