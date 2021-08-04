## Python Essentials 2 Module 4 Test

1. Which program will produce the following output:
```
Mo Tu We Th Fr Sa Su
```
answer:
```python
import calendar
print(calendar.weekheader(2))
```

2. What is the expected result of the executing the following code?
```python
def fun(n):
  s = '+'
  for i in range(n):
    s += s
    yield s
    
for x in fun(2):
  print(x, end='')
```
> It will print `++++++`

3. Look at the code below:
```python
my_tuple = (0, 1, 2, 3, 4, 5, 6)
# Insert line of code here.
print(foo)
```
Which snippet would you insert in order for the program to output the following result (list):
```
[2, 3, 4, 5, 6]
```
> `foo = list(filter(lambda x: x-0 and x-1, my_tuple))`

4. What is the expected output of the following code?
```python
import os

os.mkdir('tumbnails')
os.chdir('tumbnails')

sizes = ['small', 'medium', 'large']

for size in sizes:
  os.mkdir(size)
  
print(os.listdir())
```
> `['large', 'small', 'medium']`

5. What is the expected output of the following code?
```python
from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)
```
> `345 days, 0:00:00`

6. Look at the code below:
```python
mi_list = [1, 2, 3]
# Insert line of code here.
print(foo)
```
Which snippet would you insert in order for the program to output the following result (tuple):
```
(1, 4, 27)
```
> `foo = tuple(map(lambda x: x**x, my_list))`

7. What is the expected output of the following code?
```python
import os

os.mkdir('pictures')
os.chdir('pictures')
os.mkdir('tumbnails')
os.chdir('tumbnails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd())
```
> The path to the `pictures` directory

8. What is the expected result of the following code?
```python
import calendar

c = calendar.Calendar()

for weekday in c.iterweekdays():
  print(weekday, end=" ")
```
> `0 1 2 3 4 5 6`

9. What is the expected result of the following code?
```python
b = bytearray(3)
print(b)
```
> `bytearray(b'\x00\x00\x00')`

10. What is the expected result of executing the following code?
```python
def o(p):
  def q():
    return '*' * p
  return q
  
r = o(1)
s = o(2)
print(r() + s())
```
> It will print `***`

11. What is the expected output of the following code?
```python
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S')
```
> `19/November/27 11:27:22`

12. What is the expected result of executing the following code?
```python
def I():
  s = 'abcdef'
  for c in s[::2]:
    yield c
    
for x in I():
  print(x, end='')
```
> It will print `ace`

13. Which of the following open modes allow you to perform **read** operations? (Select two answers)
> - `r+`
> - `r`

14. Select the true statements. (Select two answers)
> - The `lambda` function can evaluate **only one** expression
> - The `lambda` function can accept **any number** of arguments

15. What is teh meaning of the value represented by `errno.EEXIST`?
> File exists

16. What keyword would you see to define an anonymous function?
> `lambda`









