def read_int(prompt, min, max):
    # Write your code here.
    while True:
        try:
            number = int(input(prompt))
            if number < min or number > max:
                print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
            else:
                return number
        except:
            print("Error: wrong input")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
