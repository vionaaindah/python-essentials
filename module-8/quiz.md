## Python Essentials 2 Module 4 Quiz

1. What is the excepted output of the following code?
```python
def my_fun():
  for num in range(3):
    yield num
    
for i in my_fun():
  print(i)
```
answer:
```
0
1
2
```

2. What is the excepted output of the following code?
```python
foo = [i + i for i in range(5)]
print(foo)
```
> `[0, 2, 4, 6, 8]`

3. What is the excepted output of the following code?
```python
x = lambda a, b: a ** b
print(x(2, 10))
```
> `1204`

4. Select the true statements about the `map()` function. (Select two answers)
> - The `map()` function can accept **more than** two arguments
> - The second `map()` function argument can be list

5. Select the true statements about the `filter()` function. (Select two answers)
> - The `filter()` function returns an iterator
> - The `filter()` function has the following syntax: `filter(function, iterable)`

6. What is the excepted output of the following code?
```python
numbers = (1, 2, 5, 9, 15)

def filter_numbers(num):
  nums = (1, 5, 17)
  if num in nums:
    return True
  else:
    return False
    
filtered_numbers = filter(filter_numbers, numbers)
for n in filtered_numbers:
  print(n)
```
answer:
```
1
5
```

7. Which of the following statements are true? (Select two answers)
> - The `map()` function creates a copy of its second argument, and applies the first argument to it
> - A list comprehension becomes a generator when used inside round brackets (i.e., `()`), not square brackets (i.e., `[]`)

8. The two basic, mutually exclusive, file open modes are named:
> binary and text

9. A method able to read data from a file into a byte array object, is named:
> `readinto()`

10. What happens if you run the following code, assuming that the `d` directory already exists?
```python
import os
os.mkdir("/a/b/c/d")
```
> A `FileExistsError` exception will be raised

11. What happens if you run the following code?
```python
import time

time.sleep(30)
print("Wake up!")
```
> The string `Wake up!` will be displayed on the screen after 30 seconds

12. What is the excepted output of the following code?
```python
import calendar

cal = calendar.isleap(2019)
print(cal)
```
> `False`
