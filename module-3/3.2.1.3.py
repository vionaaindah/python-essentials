secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Enter a number: "))
while guess_number != secret_number:
    print("Haha! You're stuck in my loop!")
    guess_number = int(input("Enter a number again: "))

print("Well done, muggle! You are free now.")
