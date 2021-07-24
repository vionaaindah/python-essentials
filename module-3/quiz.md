## Module 3 Quiz

1. An operator able to check whether two values are nor equal is coded as:
> `!=`

2. How many stars will the following snippet send to the console?
```python
i = 2
while i >= 0:
    print("*")
    i -= 2
```
> two

3. How many hashes will the following snippet send to the console?
```python
for i in range(-1, 1):
    print("#")
```
> two

4. What value will be assigned to the `x` variable?
```python
z = 10
y = 0
x = z > y or z == y
```
> `True`

5. What is the output of the following code?
```python
my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)
```
> `[3, 1, 1]`

6. The second assignment:
```python
vals = [0, 1, 2]
vals[0], vals[1] = vals[1], vals[2]
```
> doesn't change the list's length

7. Take a look at the snippet and choose one of the following statements which is true:
```python
nums = []
vals = nums
vals.append(1)
```
> `nums` and `vals` are of the same length

8. Take a look at the snippet and choose one of the following statements which is true:
```python
nums = []
vals = nums[:]
vals.append(1)
```
> `vals` is longer than `nums`

9. How many elements does the `my_list` list contain?
```python
my_list = [0 for i in range(1, 3)]
```
> two

10. What is the output of the following snippet?
```python
my_list = [0, 1, 2, 3]
x = 1
for elem in my_list:
    x *= elem
print(x)
```
> `0`
