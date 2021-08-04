## Python Essentials Final Test

1. The meaning of a *keyword argument* is determined by its:
> both name and value assigned to it

2. What is the expected behavior of the following snippet?
```python
try:
  raise Exception
except:
  print("c")
except BaseException:
  print("a")
except Exception:
  print("b")
```
> The code will cause an error

3. Select the true statements. (Select two answers)
> - If a class contains the `__init__` method, it **cannot** return any value
> - The first parameter of a class method does **not** have to be named *self*

4. Knowing that the function named `f()` resides in the module named `m`, and the code contains the following `import` statement:
```python
from f import m
```
Choose the right way to invoke the function:
> The function cannot be invoked because the `import` statement is invalid

5. What is the expected output of the following snippet?
```python
class X:
  pass
  
class Y(X):
  pass
  
class Z(Y):
  pass
  
x = X()
z = Z()
print(isinstance(x, Z), isinstance(z, X))
```
> `False True`

6. What is the expected behavior of the following piece of code?
```python
x = 16
while x > 0:
  print('*', end='')
  x //= 2
```
> The code will output `*****`

7. What is the expected behavior of the following code snippet?
```python
my_list = [1, 2, 3, 4]

my_list = list(map(lambda x: 2*x, my_list))
print(my_list)
```
> The code will output `2 4 6 8`

8. What is the expected behavior of the following piece of code?
```python
d = {1: 0, 2: 1, 3: 2, 0: 1}
x = 0

for y in range(len(d)):
  x = d[x]
  
print(x)
```
> The code will output `0`

9. Which line properly invokes the function defined as below?
```python
def fun(a, b, c=0):
  # function body
```
> `fun(a=1, b=0, c=0)`

10. What is PEP 8?
> A document that provides coding conventions and style guide for Python code

11. What is the expected behavior of the following snippet?
```python
def fun(x):
  return 1 if x % 2 != 0 else 2
  
print(fun(fun(1)))
```
> The program will output `1`

12. If you want to write a byte array's content to a stream, which method can you use?
> `write()`

13. What is the expected output of the following code?
```python
from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta)
```
> `14 days, 11:00:00`

14.Is `s` is a stream opened in read mode, the following line:
```python
q = s.readlines()
```
will assign `q` as a:
> list

15. What is the expected output of the following snippet?
```python
a = True
b = False
a = a or b
b = a and b
a = a or b
print(a, b)
```
> `True False`

16. What is the expected output of the following code?
```python
t = (1, )
t = t[0] + t[0]
print(t)
```
> `2`

17. How many empty lines will the following snippet send to the console?
```python
my_list = [[c for c in range(r)] for r in range(3)]

for element in my_list:
  if len(element) < 2:
    print()
```
> `two`

18. Which of the following sentences is true about the snippet below?
```python
str_1 = 'string'
str_2 = str_1[:]
```
> `str_1` and `str_2` are different (but equal) strings

19. What is the expected output of the following code?
```python
import calendar

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
  print(weekday, end=" ")
```
> `6 0 1 2 3 4 5`

20. What is the expected behavior of the following code?
```python
x = """
"""
print(len(x))
```
> The code will output `1`

21. If there is a `finally:` branch inside the `try:` block, we can say that:
> the `finally:` branch will always be executed

22. What is the expected output of the following code?
```python
my_string_1 = 'Bond'
my_string_2 = 'James Bond'

print(my_string_1.isalpha(), my_string_2.isalpha())
```
> `True False`

23. What is the expected result of the following code?
```python
class A:
  def a(self):
    print('a')
    
class B:
  def a(Self):
    print('b')
    
class C(A, B):
  def c(self):
    self.a()
    
o = C()
o.c()
```
> The code will print `a`

24. What is the expected output of the following snippet?
```python
print(len([i for i in range(0, -2)]))
```
> `0`

25. What is true about the following line of code?
```python
print(len((1, )))
```
> The code will output `1`

26. What is the expected output of the following piece of code if the user enters two lines containing `1` and `2` respectively?
```python
y = input()
x = input()
print(x + y)
```
> `21`

27. What is the expected output of the following code?
```python
def fun(n):
  s = ''
  for i in range(n):
    s += '*'
    yield s
    
for x in fun(3):
  print(x, end='')
```
> `******`

28. What is the `sys.stdout` stream normally associated with?
> The screen

29. What is the expected result of executing the following code?
```python
class A:
  def __init__(self):
    pass
    
  def f(self):
    return 1
    
  def g():
    return self.f()
    
a = A()
print(a.g())
```
> The code will raise an exception

30. What is the expected output of the following snippet?
```python
d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]

for x in d.keys():
  print(d[x][1]. end="")
```
> `24`

31. What is true about the following piece of code?
```python
print("a", "b", "c", sep="'")
```
> The code will output `a'b'c`

32. The `Exception` class contains a property named `args` -what is it?
> A tuple

33.  What is true about the following snippet?
```python
def fun(d, k, v):
  d[k] = v
  
my_dictonary = {}
print(fun(my_dictionary, '1', 'v'))
```
> The code will output `None`

34. What is the expected behavior of the following snippet?
```python
my_string = 'abcdef'

def fun(s):
  del s[2]
  return s
  
print(fun(my_string))
```
> The program will cause an error

35. What is the expected behavior of the following code?
```python
x = "\"
print(len(x))
```
> The code will raise an error

36. What is the expected effect of running the following code?
```python
class A:
  def __init__(self, v):
    self._a = v + 1
    
a = A(0)
print(a._a)
```
> The code will output `1`

37. What can you do if you want to tell your module users that a particular variable should **not be accessed direcly**?
> Start its name with `_` or `__`

38. Which of the following functions provided by the `os` module are available in both Windows and Unix? (Select two answes)
> - `mkdir()`
> - `chdir()`

39. If the class constructor is declared as below:
```python
class Class:
  def __init__(self):
    pass
```
which one of the assignments is valid?
> `object = Class()`

40. What is the name of the directory/folder created by Python used to store `pyc` files?
> `__pycache__`

41. A package directory/folder may contain a file intended to initialize the package. What is its name?
> `__init__.py`

42. How many stars (`*`) will the following snippet send to the console?
```python
i = 4

while i > 0:
  i -= 2
  print("*")
  if i == 2:
    break
    
else:
  print("*")
```
> one

43. What is the expected output of the following code?
```python
class A:
  A = 1
  def __init__(self):
    self.a = 0
    
print(hasattr(A, 'A'))
```
> `True`

44. What is the expected output of the following code, located in the file `module.py`?
```python
print(__name__)
```
> `__main__`

45. What *pip* operation would you use to check Python packages have been installed so far?
> `list`

46. What is the expected output of the following code?
```python
def a(x):
  def b():
    return x + x
  return b
  
x = a('x')
y = a('')
print(x() + y())
```
> `xx`

47. What is the expected output of the following piece of code?
```python
x, y, z = 3, 2, 1
z, y, x = x, y, z
print(x, y, z)
```
> `1 2 3`

48. What value will be assigned to the `x` variable?
```python
z = 2
y = 1
x = y < z or z > y and y > z or z < y
```
> `True`

49. What is the expected output of the following snippet?
```python
d = {'one': 1, 'three': 3, 'two': 2}

for k in sorted(d.values()):
  print(k, end=' ')
```
> `1 2 3`

50. What is the expected output of the following code?
```python
d = {}
class A:
  A = 1
  def __init__(self, v=2):
    self.v = v + A.A
    A.A += 1
    
  def set(self, v):
    self.v += v
    A.A += 1
    return
    
a = A()
a.set(2)
print(a.v)
```
> `5`

51. What is the expected output of the following code?
```python
from datetime import datetime

datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%Y/%m/%d %H:%M:%S'))
```
> `2019/11/27 11:27:22`

52. What is the expected behavior of the following code?
```python
import os

os.makedirs('pictures/thumnails')
os.rmdir('pictures')
```
> The code will raise an error

53. What is the expected output of the following snippet?
```python
class A:
  def __init__(self,name):
    self.name = name
    
a = A("class")
print(a)
```
> A string ending with a long hexadecimal number

54. What is the expected output of the following snippet?
```python
try:
  raise Exception
except BaseException:
  print("a", end='')
else:
  print("b", end='')
finally:
  print("c")
```
> `ac`

55. What is the expected output of the following snippet?
```python
t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)
```
> `3`

56. Which operator would you use to check whether two values are **equal**?
> `==`

57. What is the expected result of the following code?
```python
class A:
  pass
  
class B:
  pass
  
class C(A, B):
  pass
  
print(issubclass(C, A) and issubclass(C, B))
```
> The code will print `True`

58. What is the expected output of the following code?
```python
v = 1 + 1 // 2 + 1 / 2 + 2
print(v)
```
> `3.5`

59. What is true about the followinf code snippet?
```python
def fun(par2, par1):
  return par2 + par1
  
print(fun(par2=1, 2))
```
> The code is erroneous

60. Select the true statements. (Select two answers)
> - *PyPI* is short for Python Package Index
> - *PyPI* is one of many exiting Python repositories
