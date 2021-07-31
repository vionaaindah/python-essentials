## Module 2 Python Essentials 2 Test

1. UNICODE is a standard:
> like ASCII, but much more expansive

2. The following code:
```python
print(chr(odr('z') - 2))
```
prints:
> `x`

3. The following code:
```python
print(3 * 'abc' + 'xyz')
```
prints:
> `abcabcabcxyz`

4. ASCII is:
> short for *American Standard Code for Imformation Interchange*

5. The following code:
```python
print(float("1, 3"))
```
> raises a `ValueError` exception

6. Entering the `try:` block implies that:
> some of the instructions from this block may not be executed

7. Which of the following are examples of Python built-in **concrete** exceptions? (Select two answers)
> `ImportError`
> `IndexError`

8. The unnamed `expect:` block:
> must be the last one

9. What is expected output of the following code:
```python
try:
    print("5"/0)
except ArithmeticError:
    print("arith")
except ZeroDivisionError:
    print("zero")
except:
    print("some")
```
> `some`

10.  The following code:
```python
assert var == 0
```
> will stop the program when `var != 0`

11. The following code:
```python
x = '\''
print(len(x))
```
prints:
> `1`

12. The top-most Python exception is called:
> `BaseException`

13. The following code:
```python
print(ord('c') - ord('a'))
```
prints:
> `2`

14. UTF-8 is:
> a form of encoding Unicode code points

15. The following code:
```python
print('Mike' > "Mikey")
```
prints:
> `False`
