## Module 4 Miscellaneous Labs

### Lab [4.3.1.15](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.3.1.15.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Medium

**Objectives**

- improving the student's skills in operating with files (reading)
- using data collections for counting numerous data.

**Scenario**

A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

- asks the user for the input file's name;
- reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
- prints a simple histogram in alphabetical order (only non-zero counts should be presented)

Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

samplefile.txt
```
aBc
```
the expected output should look as follows:
```
a -> 1
b -> 1
c -> 1
```

Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

### Lab [4.3.1.16](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.3.1.16.py)

**Estimated time**

15-30 minutes

**Level of difficulty**

Medium

**Prerequisites**

4.3.1.15

**Objectives**

- improve the student's skills in operating with files (reading/writing)
- using lambdas to change the sort order.

**Scenario**

The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

- the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
- the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)

Assuming that the input file contains just one line filled with:

samplefile.txt
```
cBabAa
```
the expected output should look as follows:
```
a -> 3
b -> 2
c -> 1
```

Tip: Use a lambda to change the sort order.

### Lab [4.3.1.17](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.3.1.17.py)

**Estimated time**

30-90 minutes

**Level of difficulty**

Medium

**Objectives**

- improve the student's skills in operating with files (reading)
- perfecting the student's abilities in defining and using self-defined exceptions and dictionaries.

**Scenario**

Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains three elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

The file may look as follows:

samplefile.txt
```
John	Smith	5
Anna	Boleyn	4.5
John	Smith	2
Anna	Boleyn	11
Andrew	Cox	1.5
```

Your task is to write a program which:

- asks the user for Prof. Jekyll's file name;
- reads the file contents and counts the sum of the received points for each student;
- prints a simple (but sorted) report, just like this one:
```
Andrew Cox 	 1.5
Anna Boleyn 	 15.5
John Smith 	 7.0
```

Note:

- your program must be fully protected against all possible failures: the file's non-existence, the file's emptiness, or any input data failures; encountering any data error should cause immediate program termination, and the erroneous should be presented to the user;
- implement and use your own exceptions hierarchy - we've presented it in the editor; the second exception should be raised when a bad line is detect, and the third when the source file exists but is empty.

Tip: Use a dictionary to store the students' data.

### Lab [4.4.1.8](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.4.1.8.py)

**Estimated time**

15-30 min

**Level of difficulty**

Easy

**Objectives**

- improving the student's skills in interacting with the operating system;
- practical use of known functions provided by the os module.

**Scenario**

It goes without saying that operating systems allow you to search for files and directories. While studying this part of the course, you learned about the functions of the os module, which have everything you need to write a program that will search for directories in a given location.

To make your task easier, we have prepared a test directory structure for you:

![image](https://user-images.githubusercontent.com/69779014/128511386-d8c51683-9063-4c53-ac94-73c68ba70c8d.png)

Your program should meet the following requirements:

1. Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
2. The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.

Example input:
```
path="./tree", dir="python"
```
Example output:
```
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python
```

### Lab [4.5.1.22](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.5.1.22.py)

**Estimated time**

15-45 min

**Level of difficulty**

Easy

**Objectives**

- improving the student's skills in date and time formatting;
- improving the student's skills in using the strftime method.

**Scenario**

During this course, you learned about the strftime method, which requires knowledge of directives to create a format. It's time to put the known directives into practice.

By the way, you'll have the opportunity to practice working with documentation, because you'll have to find directives that you don't yet know.

Here's your task:

Write a program that creates a datetime object for November 4, 2020 , 14:53:00. The object created should call the strftime method with the appropriate format to display the following result:
```
2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Weekday: 3
Day of the year: 309
Week number of the year: 44
```

Note: Each result line should be created by calling the strftime method with at least one directive in the format argument.

### Lab [4.6.1.13](https://github.com/vionaaindah/python-essentials/blob/main/module-6/4.6.1.13.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Easy

**Objectives**

- Improving the student's skills in using the Calendar class

**Scenario**

During this course, we looked at the Calendar class a bit. Your task is to extend its functionality with a new method called `count_weekday_in_year`, which takes a year and a weekday as parameters, and then returns the number of occurrences of a specific weekday in the year.

Use the following tips:

- Create a class called `MyCalendar` that extends the `Calendar` class;
- create the `count_weekday_in_year` method with the year and weekday parameters. The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday. The method should return the number of days as an integer;
- in your implementation, use the `monthdays2calendar` method of the Calendar class.

The following are the expected results:

Sample arguments
```
year=2019, weekday=0
```
Expected output
```
52
```

Sample arguments
```
year=2000, weekday=6
```
Expected output
```
53
```
