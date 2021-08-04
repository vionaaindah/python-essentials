## Part 1 Summary Test

1. Assuming that `my_tuple` is a correctly created tuple, the fact that tuples are immutable means that the following instruction:
```python
my_tuple[1] = my_tuple[1] + my_tuple[0]
```
> is illegal

2. How many elements does  the `lst` list contain?
```python
lst = [i for i in range(-1, -2)]
```
> `zero`

3. How many stars (`*`) will the following snippet send to the console?
```python
i = 0
while i < i + 2:
  i += 1
  print("*")
else:
  print("*")
```
> the snippet will enter an infinite loop, printing one star per line

4. Which of the following sentences are true about the code? (Select two answer)
```python
nums = [1, 2, 3]
vals = nums
```
> - `nums` has the same length as `vals`
> - `nums` and `vals` are different names of the same list

5. What is the output of the following snippet?
```python
def fun(x, y):
  if x == y:
    return x
  else:
    return fun(x, y-1)
    
print(fun(0, 3))
```
> `0`

6. The meaning of a *positional argument* is determined by:
> its position within the argument list

7. What is the output of the following snippet?
```python
def fun(x):
  if x % 2 == 0:
    return 1
  else:
    return 2
    
print(fun(fun(2)))
```
> `2`

8. The following snippet:
```python
def function_1(a):
  return None
  
def function_2(a):
  return function_1(a) * function_1(a)
  
print(function_2(2)
```
> will cause a runtime error

9. What is the output of the following piece of code?
```python
print("a", "b", "c", sep="sep")
```
> `asepbsepc`

10. An operator able to check whether two values are not equal is coded as:
> `!=`

11. How many hashes (`#`) will the following snippet send to the console?
```python
lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
  for c in range(3):
    if lst[r][c] % 2 != 0:
      print("#")
```
> `three`

12. What is the output of the following snippet?
```python
my_list = [x * x for x in range(5)]

def fun(lst):
  del lst[lst[2]]
  return lst
  
print(fun(my_list))
```
> `0, 1, 4, 9`

13. What is the output of the following snippet?
```python
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
  print(dct[x][1], end="")
```
> `21`

14. What is the output of the following piece of code?
```python
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
```
> `1 1 2`

15. Which of the following lines correctly invoke the function defined below? (Select two answers)
```python
def fun(a, b, c=0):
  # Body of the function.
```
> - `fun(0, 1, 2)`
> - `fun(b=0, a=0)`

16. The result of the following division:
`1 // 2`
> is equal to `0`

17. What is the output of the following snippet?
```python
dd = {"1": "0", "0": "1"}
for x in dd.vals():
  print(x, end="")
```
> the code is erroneous (the `dict` object has no `vals()` method)

18. What is the output of the following piece of code if the user enters two lines containing `3` and `6` respectively?
```python
y = input()
x = input()
print(x + y)
```
> `63`

19. The following snippet:
```python
def func(a, b):
  return b ** a
  
print(func(b=2, 2))
```
> is erroneous

20. What is the output of the following snippet?
```python
def fun(inp=2, out=3):
  return inp * out
  
print(fun(out=2))
```
> `4`

21. What is the output of the following piece of code if the user enters two lines containing `2` and `4` respectively?
```python
x = float(input())
y = float(input())
print(y ** (1 / x))
```
> `2.0`

22. Which of the following variable names are illegal and will cause the SyntaxError exeption? (Select two answers)
> - `for`
> - `in`

23. What value will be assigned to the `x` variable?
```python
z = 0
y = 10
x = y < z and z > y or y > z and z < y
```
> `True`

24.  What is the output of the following snippet?
```python
my_list = [1, 2]

for v in range(2):
  my_list.insert(-1, my_list[v])
  
print(my_list)
```
> `[1, 1, 1, 2]`

25.  What is the output of the following snippet?
```python
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
```
> `4`

26. What is the output of the following piece of code?
```python
x = 1 // 5 + 1 / 5
print(x)
```
> `0.2`

27. What is the output of the following piece of code if the user enters two lines containing `3` and `2` respectively?
```python
x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
```
> `0`

28. Take a look at the snippet and choose the true statement:
```python
nums = [1, 2, 3]
vals = nums
del vals[:]
```
> `nums` and `vals` have the same length

29. What is the output of the following snippet?
```python
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
  v = dct[v]
  
print(v)
```
> `one`

30. What is the output of the following snippet?
```python
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)
```
> `0 1`
