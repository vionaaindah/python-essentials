hidden = input("Enter the first word: ")
string = input("Enter the second word: ")

hidden_char = ''.join(sorted(set(hidden.lower()))).strip()
string_char = ''.join(sorted(set(string.lower()))).strip()

if hidden_char in string_char:
    print("Yes")
else:
    print("No")
