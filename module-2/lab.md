## Module 2 Data types, variables, basic input-output operations, basic operators Labs

### Lab [2.1.1.6](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.1.1.6.py)

**Estimated time**

5-10 minutes

**Level of difficulty**

Very easy

**Objectives**

- becoming familiar with the print() function and its formatting capabilities;
- experimenting with Python code.

**Scenario**

The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

In your first lab:

- use the print() function to print the line Hello, Python! to the screen. Use double quotes around the string;
- having done that, use the print() function again, but this time print your first name;
- remove the double quotes and run your code. Watch Python's reaction. What kind of error is thrown?
- then, remove the parentheses, put back the double quotes, and run your code again. What kind of error is thrown this time?
- experiment as much as you can. Change double quotes to single quotes, use multiple print() functions on the same line, and then on different lines. See what happens.

### Lab [2.1.1.18](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.1.1.18.py)

**Estimated time**

5-10 minutes

**Level of difficulty**

Very easy

**Objectives**

- becoming familiar with the print() function and its formatting capabilities;
- experimenting with Python code.

**Scenario**

The print() command, which is one of the easiest directives in Python, simply prints out a line to the screen.

**Expected output**
```
Programming***Essentials***in...Python
```

### Lab [2.1.1.19](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.1.1.19.py)

**Estimated time**

5-10 minutes

**Level of difficulty**

Easy

**Objectives**

- experimenting with existing Python code;
- discovering and fixing basic syntax errors;
- becoming familiar with the print() function and its formatting capabilities.

**Scenario**

We strongly encourage you to play with the code we've written for you, and make some (maybe even destructive) amendments. Feel free to modify any part of the code, but there is one condition - learn from your mistakes and draw your own conclusions.

Try to:

- minimize the number of print() function invocations by inserting the \n sequence into the strings
- make the arrow twice as large (but keep the proportions)
- duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
- remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error - is this the place where the error really exists?
- do the same with some of the parentheses;
- change any of the print words into something else, differing only in case (e.g., Print) - what happens now?
- replace some of the quotes with apostrophes; watch what happens carefully.

### Lab [2.2.1.11](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.2.1.11.py)

**Estimated time**

5-10 minutes

**Level of difficulty**

Easy

**Objectives**

- becoming familiar with the print() function and its formatting capabilities;
- practicing coding strings;
- experimenting with Python code.

**Scenario**

Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.

**Expected output**
```
"I'm"
""learning""
"""Python"""
```

### Lab [2.4.1.7](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.4.1.7.py)

**Estimated time**

10 minutes

**Level of difficulty**

Easy

**Objectives**

- becoming familiar with the concept of storing and working with different data types in Python;
- experimenting with Python code.

**Scenario**

Here is a short story:

Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.

Your task is to:

- create the variables: john, mary, and adam;
- assign values to the variables. The values must be equal to the numbers of fruit possessed by John, Mary, and Adam respectively;
- having stored the numbers in the variables, print the variables on one line, and separate each of them with a comma;
- now create a new variable named total_apples equal to addition of the three former variables.
- print the value stored in total_apples to the console;
- experiment with your code: create new variables, assign different values to them, and perform various arithmetic operations on them (e.g., +, -, *, /, //, etc.). Try to print a string and an integer together on one line, e.g., "Total number of apples:" and total_apples.

### Lab [2.4.1.9](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.4.1.9.py)

**Estimated time**

10 minutes

**Level of difficulty**

Easy

**Objectives**

- becoming familiar with the concept of, and working with, variables;
- performing basic computations and conversions;
- experimenting with Python code.

**Scenario**

Miles and kilometers are units of length or distance.

Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:

- miles to kilometers;
- kilometers to miles.

Do not change anything in the existing code. Write your code in the places indicated by ###. Test your program with the data we've provided in the source code.


Pay particular attention to what is going on inside the print() function. Analyze how we provide multiple arguments to the function, and how we output the expected data.

Note that some of the arguments inside the print() function are strings (e.g., "miles is", whereas some other are variables (e.g., miles).

**_TIP_**

There's one more interesting thing happening there. Can you see another function inside the print() function? It's the round() function. Its job is to round the outputted result to the number of decimal places specified in the parentheses, and return a float (inside the round() function you can find the variable name, a comma, and the number of decimal places we're aiming for). We're going to talk about functions very soon, so don't worry that everything may not be fully clear yet. We just want to spark your curiosity.


After completing the lab, open Sandbox, and experiment more. Try to write different converters, e.g., a USD to EUR converter, a temperature converter, etc. - let your imagination fly! Try to output the results by combining strings and variables. Try to use and experiment with the round() function to round your results to one, two, or three decimal places. Check out what happens if you don't provide any number of digits. Remember to test your programs.

Experiment, draw conclusions, and learn. Be curious.


**Expected output**
```
7.38 miles is 11.88 kilometers
12.25 kilometers is 7.61 miles
```

### Lab [2.4.1.10](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.4.1.10.py)

**Estimated time**

10-15 minutes

**Level of difficulty**

Easy

**Objectives**

- becoming familiar with the concept of numbers, operators, and arithmetic operations in Python;
- performing basic calculations.

**Scenario**

Take a look at the code in the editor: it reads a float value, puts it into a variable named x, and prints the value of a variable named y. Your task is to complete the code in order to evaluate the following expression:

3x3 - 2x2 + 3x - 1

The result should be assigned to y.

Remember that classical algebraic notation likes to omit the multiplication operator - you need to use it explicitly. Note how we change data type to make sure that x is of type float.

Keep your code clean and readable, and test it using the data we've provided, each time assigning it to the x variable (by hardcoding it). Don't be discouraged by any initial failures. Be persistent and inquisitive.


**Test Data**

Sample input
```
x = 0
x = 1
x = -1
```
Expected output
```
y = -1.0
y = 3.0
y = -9.0
```

### Lab [2.5.1.2](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.5.1.2.py)

**Estimated time**

5 minutes

**Level of difficulty**

Very Easy

**Objectives**

- becoming familiar with the concept of comments in Python;
- using and not using comments;
- replacing comments with code;
- experimenting with Python code.

**Scenario**

The code in the editor contains comments. Try to improve it: add or remove comments where you find it appropriate (yes, sometimes removing a comment can make the code more readable), and change variable names where you think this will improve code comprehension.

**_NOTE_**

Comments are very important. They are used not only to make your programs easier to understand, but also to disable those pieces of code that are currently not needed (e.g., when you need to test some parts of your code only, and ignore other). Good programmers describe each important piece of code, and give self-commenting names to variables, as sometimes it is simply much better to leave information in the code.

It's good to use readable variable names, and sometimes it's better to divide your code into named pieces (e.g., functions). In some situations, it's a good idea to write the steps of computations in a clearer way.

One more thing: it may happen that a comment contains a wrong or incorrect piece of information - you should never do that on purpose!

### Lab [2.6.1.10](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.6.1.10.py)

**Estimated time**

20 minutes

**Level of difficulty**

Intermediate

**Objectives**

- becoming familiar with the concept of numbers, operators and arithmetic operations in Python;
- understanding the precedence and associativity of Python operators, as well as the proper use of parentheses.

**Scenario**

Your task is to complete the code in order to evaluate the following expression:

![image](https://user-images.githubusercontent.com/69779014/128478538-18abd98b-2cf9-455d-bc96-ff51d0d5a2fa.png)

The result should be assigned to y. Be careful - watch the operators and keep their priorities in mind. Don't hesitate to use as many parentheses as you need.

You can use additional variables to shorten the expression (but it's not necessary). Test your code carefully.

**Test Data**

Sample input: `1`

Expected output:
```
y = 0.6000000000000001
```
Sample input: `10`

Expected output:
```
y = 0.09901951266867294
```
Sample input: `100`

Expected output:
```
y = 0.009999000199950014
```
Sample input: `-1`

Expected output:
```
y = -0.19258202567760344
```

### Lab [2.6.1.11](https://github.com/vionaaindah/python-essentials/blob/main/module-2/2.6.1.11.py)

**Estimated time**

15-20 minutes

**Level of difficulty**

Easy

**Objectives**

- improving the ability to use numbers, operators, and arithmetic operations in Python;
- using the print() function's formatting capabilities;
- learning to express everyday-life phenomena in terms of programming language.

**Scenario**

Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

Don't worry about any imperfections in your code - it's okay if it accepts an invalid time - the most important thing is that the code produce valid results for valid input data.

Test your code carefully. Hint: using the % operator may be the key to success.

**Test Data**

Sample input:
```
12
17
59
```
Expected output: `13:16`

Sample input:
```
23
58
642
```
Expected output: `10:40`

Sample input:
```
0
1
2939
```
Expected output: `1:0`






