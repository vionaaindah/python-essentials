my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Write your code here.
tmp_list = []

for i in my_list:
    if i not in tmp_list:
        tmp_list.append(i)
        
my_list = tmp_list

print("The list with unique elements only:")
print(my_list)
