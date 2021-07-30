first_word = input("Enter the first word: ")
second_word = input("Enter the second word: ")

if sorted(first_word.upper()) == sorted(second_word.upper()):
    print("Anagrams")
else:
    print("Not anagrams")        
