text = input("Enter the text : ")
reverse = ""
text = text.replace(" ", "")
text = text.upper()

for i in text:
    reverse = i + reverse  

if text == reverse:
   print("It's a palindrome")
else:
   print("It's not a palindrome")
