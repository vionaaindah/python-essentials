## Module 3 Python Essentials 2 Test

1. What will be the result of executing the following code?
```python
def f(x):
  try:
    x = x / x
  except:
    print("a",end'')
  else:
    print("b",end'')
  finally:
    print("c",end'')

f(1)
f(0)
```
> it will print `bcac`

2. What will be the result of executing the following code?
```python
class A:
  def __str__(self):
    return 'a'

class B(A):
  def __str__(self):
    return 'b'
    
class C(B):
  pass
  
o = C()
print(o)
```
> it will be print `b`

3. What will be the effect of running the following code?
```python
class A:
  def __init__(self,v):
    self.__a = v + 1
    
a = A(0)
print(a.__a)
```
> The code will raise an `AttributeError` exception

4. What will be the result of executing the following code?
```python
class A:
  v = 2

class B(A):
  v = 1
    
class C(B):
  pass
  
o = C()
print(o.v)
```
> it will return `1`

5. What will be the result of executing the following code?
```python
class A:
  def __init__(self):
    pass
    
a = A(1)
print(hasattr(a,'A'))
```
> it will raise an exception

6. What will be the result of executing the following code?
```python
try:
  raise Exception(1,2,3)
except Exception as e:
  print(len(a.args))
```
> it will print `3`

7. If the class's constructor is declared as below, which one of the assignments is valid?
```python
class Class:
  def __init__(self):
    pass
```
> `object = Class()`

8. What will be the result of executing the following code?
```python
class Ex(Exception):
  def __init__(self,msg):
    Exception.__init__(self,msg + msg)
    self.args = (msg,)
    
try:
  raise Ex('ex')
except Ex as e:
  print(e)
except Exception as e:
  print(e)
```
> it will be print `ex`

9. What will be the result of executing the following code?
```python
class A:
  pass

class B(A):
  pass
    
class C(B):
  pass
  
print(issubclass(C,A))
```
> it will be print `True`

10. What will be the output of the following code?
```python
class A:
  def __init__(self,v = 1):
    self.v = v
    
  def set(self,v):
    self.v = v
    return v
    
a = A()
print(a.set(a.v + 1))
```
> `2`

11. What will be the result of executing the following code?
```python
class A:
  def a(self):
    print('a')

class B(A):
  def a(self):
    print('b')
    
class C(B,A):
  def c(self):
    self.a()
  
o = C()
o.c()
```
> it will be print `b`

12. What will be the output of the following code?
```python
class A:
  A = 1
  
  
print(hasattr(A,'A'))
```
> `True`

13. What will be the output of the following code?
```python
class A:
  X = 0
  def __init__(self,v = 0):
    self.Y = v
    A.X += v
    
a = A()
b = A(1)
c = A(2)
print(c.X)
```
> `3`

14. If there is a superclass named `A` and a subclass named `B`, which one of the presented invocations should you put instead of the comment?
```python
class A:
  def __init__(self):
    self.a = 1
    
class B(A):
  def __init__(self):
    # Put selected line here.
    self.b = 2
```
> `A.__init__(self)`

15. What will be the result of executing the following code?
```python
class A:
  def __str__(self):
    return 'a'

class B(A):
  def __str__(self):
    return 'b'
    
class C(A,B):
  pass
  
o = C()
print(o)
```
> it will print `a`

16. A data structure described as *LIFO* is actually a:
> stack
