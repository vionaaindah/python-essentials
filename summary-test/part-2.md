## Part 2 Summary Test

1. What is the expected result of the following code?
```python
from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)
```
> `28 days, 22:00:00`

2. The following line of code:
```python
for line in open('text.txt', 'rt'):
```
> is **valid** because `open` returns an iterable object

3. What is the expected result of the following code?
```python
class A:
  def __init__(self):
    pass
    
a = A(1)
print(hasattr(a,'A'))
```
> The code will raise an exception

4. If the class constructor is declared in the following way:
```python
class Class:
  def __init__(self, val=0):
    pass
```
which one of the assignments is **invalid**?
> `object = Class(1, 2)`

5. The following code:
```python
x = "\\\\"
print(len(x))
```
> will print `2`

6. The compiled Python bytecode is stored in files which have their names ending with:
> `pyc`

7. The following statement:
```python
from a.b import c
```
causes the import of:
> entity `c` from module `b` from package `a`

8. What is the expected output of the following code?
```python
class A:
  A = 1
  def __init__(self):
    self.a = 0
    
print(hasattr(A, 'a'))
```
> `False`

9. What is the expected result of the following snippet?
```python
try:
  raise Exception
except:
  print("c")
except BaseException:
  print("a")
except Exception:
  ptint("b")
```
> The code will cause a syntax error

10. The following code:
```python
print(chr(ord('p') + 2))
```
will print:
> `r`

11. Look at the code below:
```python
import random

#
# Insert lines of code here.
#

print(a, b, c)
```
Which of the code would you insert so that it is possible for the program to output the following result:
```
6 81 0
```
answer:
```python
a = random.randint(0, 100)
b = random.randrange(10, 100, 3)
c random.choice((0, 100, 3))
```

12. WHat will be the output of the following code, located in the `p.py` file?
```python
print(__name__)
```
> `__main__`

13. The `sys.stderr` stream is normally associated with:
> the screen

14. Look at the following code:
```python
numbers = [i*i for i in range(5)]
# Insert lines of code here.
print(foo)
```
Which line would you insertin order for the program to produce the expected output?
```
[1, 9]
```
> `foo = list(filter(lambda x: x % 2, numbers))

15. What is the expected result of executing the following code?
```python
try:
  raise Exception(1, 2, 3)
except Exception as e:
  print(len(e.args))
```
> The code will print `3`

16. The following statement:
```python
assert var != 0
```
> will stop program when `var == 0`

17. What is the expected result of executing the following code?
```python
class A:
  def a(self):
    print('a')

class B:
  def a(self):
    print('b')

class C(B, A):
  def c(self):
    self.a()
    
o = C()
o.c()
```
> The code will print `b`

18. If there are more than one `except:` branches after the `try:` clause, we can say that:
> **not more than one** `except:` block will be executed

19. What is the expected result of executing the following code?
```python
import calendar

calendar.setfirstweekdar(calendar.SUNDAY)
print(calendar.weekheader(3))
```
> `Sun Mon Tue Wed Thu Fri Sat`

20. What is the expected result of executing the following code?
```python
from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)
```
> `11:27:22`

21. Knowing that a function named `fun()` resides in a module named `mod`, and was imported using the following statement:
```python
from mod import fun
```
Choose the right way to invoke the `fun()` function:
> `fun()`

22.  What is the expected result of executing the following code?
```python
import os

os.mkdir('pictures')
os.chdir('pictures')

print(os.getcwd())
```
> The code will print the path to the created directory

23. Which `pip` command would you use to uninstall a previously installed package?
> `pip uninstall packagename`

24. Look at the following code:
```python
numbers = [0, 2, 7, 9, 10]
# Insert lines of code here.
print(list(foo))
```
Which line would you insertin order for the program to produce the expected output?
```
[0, 4, 49, 81, 100]
```
> `foo = map(lambda num: num ** 2, numbers)`

25. What information can be read using the `uname` function provided by the `os` module? (Slect two answers)
```python
import os

os.mkdir('pictures')
os.chdir('pictures')

print(os.getcwd())
```
> - Operating system name
> - Hardware identifier

26. What is the expected result of executing the following code?
```python
class I:
  def __init__(self):
    self.s = 'abc'
    self.i = 0
    
    def __iter__(self):
    return self
      
  def __next__(self):
    if self.i == len(self.s):
      raise StopIteration
    v = self.s[self.i]
    self.i += 1
    return v
    
for x in I():
  print(x, end='')
```
> The code will print `abc`

27. If you want to fill a byte array with data read in from a stream, which method can you use?
> The `readinto()` method

28. What is the expected result of executing the following code?
```python
class A:
  pass

class B:
  pass
  
class C(B):
  pass
  
print(issubclass(A, C))
```
> The code will print `False`

29. The following code:
```python
print(float("1.3"))
```
> will print `1.3`

30. Is `s` is a stream opened in *read* mode, the following line:
```python
q = s.read(1)
```
will read:
> one character from the stream

31. What is the expected result of executing the following snippet?
```python
try:
  raise Exception
except BaseException:
  print("a")
except Exception:
  print("b")
except:
  print("c")
```
> `a`

32. Assuming that the following three files: `a.py`, `b.py`, and `c.py` reside in the same directory, what will be the output produced after running the `c.py` file?
```python
# file a.py
print("a", end='')

# file b.py
print("b, end='')

# file c.py
print("c", end='')
import a
import b
```
> `cab`

33. What is the expected result of executing the following code?
```python
def my_fun(n):
  s = '+'
  for i in range(n):
    s += s
    yield s
    
for x in my_fun(2)
  print(x, end='')
```
> The code will print `++++++`

34. What is the expected result of executing the following code?
```python
def o(p):
  def q():
    return '*' * p
  return q
  
r = o(1)
s = o(2)
print(r() + s())
```
> The code will print `***`

35. What is the expected result of executing the following code?
```python
class A:
  def __init__(self, v=2):
    self.v = v
    
  def set(self, v=1):
    self.v += v
    return self.v
    
a = A()
b = a
b.set()
print(a.v)
```
> `3`

36. What output will appear after running the following snippet?
```python
import math
print(dir(math))
```
> A list of all the entities residing in the `math` module

37. Assuming that the `open()` invocation has gone successfully, the following snippet:
```python
for x in open('file', 'rt'):
  print(x)
```
will:
> read the file line by line

38. The following code:
```python
x = "\\\"
print(len(x))
```
> will cause an error

39. Which of the following commands would you use to check `pip`'s version? (Select two answers)
> - `pip --version`
> - `pip3 --version`

40. What is the expected effect of running the following code?
```python
class A:
  def __init__(self, v):
    self.__a = v + 1
    
a = A(0)
print(a.__a)
```
> The code will raise an `AttributeError` exception
