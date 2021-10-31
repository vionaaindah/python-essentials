## Module 4 Test

1. What is the output of the following snippet?
```python
def fun(x, y, z)
  return x + 2 * y + 3 * z
  
print(fun(0, z=1, y=3))
```
> `9`

2. Assuming that `my_tuple` is a correctly created tuple, the fact that tuples are immutable means taht the following instruction:
```python
my_tuple[1] = my_tuple[1] + my_tuple[0]
```
> is illegal

3. What is the output of the following snippet?
```python
def fun(x)
  x += 1
  return x
  
x = 2
x = fun(x + 1)
print(x)
```
> `4`

4. A built-in function is a function which:
> comes with Python, and is an integral part of Python

5. The fact that tuples belong to sequence types means that:
> they can be indexed and sliced like lists

6. What is the output of the following snippet?
```python
def fun(x):
  if x % 2 == 0:
    return 1
  else:
    return

print(fun(fun(2)) + 1)
```
> the code will cause a runtime error

7. The following snippet:
```python
def func(a, b):
  return a ** a
  
print(func(2))
```
> is erroneous

8. A function defined in the following way: (Select two answer)
```python
def function(x=0):
  return x
```
> - may be invoked without any argument
> - may be involked with exactly one argument

9. The following snippet:
```python
def func_1(a):
  return a ** a
  
def func_2(a):
  return func_1(a) * func_1(a)
  
print(func_2(2))
```
> will output `16`

10. What code would you insert instead of the comment to obtain the expected output?
Expected output:
```python
a
b
c
```
Code:
```python
dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
  dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
  k = dictionary[i]
  # Insert your code here.
```
> `print(k[0])`

11. What is the output of the following snippet?
```python
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
```
> `2`

12. What is the output of the following snippet?
```python
my_list = ['Mary', 'had', 'a', 'little', 'lamb']

def my_list(my_list):
  del my_list[3]
  my_list[3] = 'ram'
  
print(my_list(my_list))
```
> no output, the snippet is erroneous

13. Which one of the following lines properly starts a parameterless function definition?
> `def fun():`

14. What is the output of the following snippet?
```python
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
  v = dictionary[v]

print(v)
```
> `two`

15. What is the output of the following snippet?
```python
def any():
  print(var + 1, end='')
  
var = 1
any()
print(var)
```
> `21`

16. What is the output of the following snippet?
```python
def fun(inp=2, out=3):
  return inp * out
  
print(fun(out=2))
```
> `4`

17. What is the output of the following snippet?
```python
def f(x):
  if x == 0:
    return 0
  return x + f(x - 1)
  
print(f(3))
```
> `6`

18. What is the output of the following snippet?
```python
def fun(x):
  global y
  y = x * x
  return y
  
fun(2)
print(y)
```
> `4`

19. Which of the following statements are true? (Select two answers)
> - The `None` value can be compared with variables
> - The `None` value can be assigned to variables

20. Which of the following lines properly starts a function using two parameters, both with zeroed default values?
> `def fun(a=0, b=0):`
