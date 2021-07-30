birth = input("Enter your Birthday (YYYMMDD): ")
dof = 0
digit_of_life = 0

for count in birth:
   dof += int(count)

for digit in str(dof):
   digit_of_life += int(digit)
   
print(digit_of_life)
