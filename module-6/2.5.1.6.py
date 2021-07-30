def encrypt(text, shift):

    result = ""

    for i in range(len(text)):
        if text[i].isupper(): # Encrypt uppercase characters
            result += chr((ord(text[i]) + shift - 65) % 26 + 65)
        elif text[i].islower(): # Encrypt lowercase characters
            result += chr((ord(text[i]) + shift - 97) % 26 + 97)
        else: # other than alpha
            result += text[i]

    return result

text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

print("Your encrypted message: " + encrypt(text, shift))
