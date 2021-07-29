## Module 1 Python Essentials Test

1. How to use `pip` to remove an installed package?
> `pip uninstall package`

2. Choose the true statements. (Select two answers)
> - The `system` function from the `platform` module returns a string with your OS name
> - The `version` function from the `platform` module returns a string with your OS version

3. The *pyc* file contains:
> compiled Python code

4. A list of package's dependencies can be obtained from `pip` using its command named:
> `show`

5. What is true about updating already installed Python packages?
> it's performed by the `install` command accompanied by the `-U` option

6. What is expected output of the following code?
```python
from random import randint

for i in range(2):
  print(randint(1, 2), end='')
```
> `11`, `12`, `21`, or `22`

7. The following statement:
```python
from a.b import c
```
causes the import of:
> entity `c` from module `b` from package `a`

8. During the first import of a module, Python deploy the *pyc* files in the directory called:
> `__pycache__`

9. The digraph written as `#!` is used to:
> tell a Unix or Unix-like OS how to execute the contents of a Python file

10. The `pip list` command presents a list of:
> locally installed packages

11. Knowing that a function named `fun()` resides in a module named `mod`, choose the correct way to import it:
> `from mod import fun`

12. What is the expected value of the result variable after the following code is executed?
```python
import math

result = math.e != math.pow(2, 4)
print(int(result))
```
> `1`

13. A function which returns a list of all entities available in a module is called:
> `dir()`

14. Knowing that a function named `fun()` resides in a module named `mod`, and it has been imported using the following line:
```python
import mod
```
Choose the way it can be invoked in your code:
> `mod.fun()`

15. When a module is imported, its contents:
> are executed once (implicitly)

16. What is the true about the `pip install` command? (Select two answers)
> - it installs a package per user only when the `--user` option is specified
> - it allows the user to install a specific version of the package

17. What is true about the `pip search` command? (Select three answers)
> - it searches through all PyPI packages
> - it needs working Internet connection to work
> - all its searches are limited to locally installed packages

18. A predefined Python variable that stores the current module name is called:
> `__name__`
