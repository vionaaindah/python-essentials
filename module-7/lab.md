## Module 3 Object-Oriented Programming Labs

### Lab [3.2.1.14](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.2.1.14.py)

**Estimated time**

20-45 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improve the student's skills in defining classes;
- using existing classes to create new classes equipped with new functionalities.

**Scenario**

We've showed you recently how to extend Stack possibilities by defining a new class (i.e., a subclass) which retains all inherited traits and adds some new ones.

Your task is to extend the `Stack` class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

- introduce a property designed to count pop operations and name it in a way which guarantees hiding it;
- initialize it to zero inside the constructor;
- provide a method which returns the value currently assigned to the counter (name it `get_counter()`).

Complete the code in the editor. Run it to check whether your code outputs 100.

### Lab [3.2.1.15](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.2.1.15.py)

**Estimated time**

20-45 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improving the student's skills in defining classes from scratch;
- implementing standard data structures as classes.

**Scenario**

As you already know, a stack is a data structure realizing the so-called LIFO (Last In - First Out) model. It's easy and you've already grown perfectly accustomed to it.

Let's taste something new now. A queue is a data model characterized by the term FIFO: First In - Fist Out. Note: a regular queue (line) you know from shops or post offices works exactly in the same way - a customer who came first is served first too.

Your task is to implement the `Queue` class with two basic operations:

- `put(element)`, which puts an element at end of the queue;
- `get()`, which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)

Follow the hints:

- use a list as your storage (just like we did in stack)
- `put()` should append elements to the beginning of the list, while `get()` should remove the elements from the list's end;
- define a new exception named `QueueError` (choose an exception to derive it from) and raise it when `get()` tries to operate on an empty list.
Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.

**Expected output**
```
1
dog
False
Queue error
```

### Lab [3.2.1.16](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.2.1.16.py)

**Estimated time**

15-30 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improving the student's skills in defining subclasses;
- adding a new functionality to an existing class.

**Scenario**

Your task is to slightly extend the Queue class' capabilities. We want it to have a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs a similar result to ours.

Below you can copy the code we used in the previous lab:
```
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    def put(self,elem):
        self.queue.insert(0,elem)
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError
```

**Expected output**
```
1
dog
False
Queue empty
```

### Lab [3.4.1.12](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.4.1.12.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improving the student's skills in defining classes from scratch;
- defining and using instance variables;
- defining and using methods.

**Scenario**

We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

- objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
- the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.

Use the following hints:

- all object's properties should be private;
- consider writing a separate function (not method!) to format the time string.

Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

**Expected output**
```
23:59:59
00:00:00
23:59:59
```

### Lab [3.4.1.13](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.4.1.13.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improving the student's skills in defining classes from scratch;
- defining and using instance variables;
- defining and using methods.

**Scenario**

Your task is to implement a class called `Weeker`. Yes, your eyes don't deceive you - this name comes from the fact that objects of that class will be able to store and to manipulate days of a week.

The class constructor accepts one argument - a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

- objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
- the class should be equipped with one-parameter methods called `add_days(n)` and `subtract_days(n)`, with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
- all object's properties should be private;

Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

**Expected output**
```
Mon
Thu
Sun
Sorry, I can't serve your request.
```

### Lab [3.4.1.14](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.4.1.14.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Easy/Medium

**Objectives**

- improving the student's skills in defining classes from scratch;
- defining and using instance variables;
- defining and using methods.

**Scenario**

Let's visit a very special place - a plane with the Cartesian coordinate system (you can learn more about this concept here: https://en.wikipedia.org/wiki/Cartesian_coordinate_system).

Each point located on the plane can be described as a pair of coordinates customarily called x and y. We expect that you are able to write a Python class which stores both coordinates as float numbers. Moreover, we want the objects of this class to evaluate the distances between any of the two points situated on the plane.

The task is rather easy if you employ the function named hypot() (available through the math module) which evaluates the length of the hypotenuse of a right triangle (more details here: https://en.wikipedia.org/wiki/Hypotenuse) and here: https://docs.python.org/3.7/library/math.html#trigonometric-functions.

This is how we imagine the class:

- it's called `Point`;
- its constructor accepts two arguments (x and y respectively), both default to zero;
- all the properties should be private;
- the class contains two parameterless methods called `getx()` and `gety()`, which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
- the class provides a method called `distance_from_xy(x,y)`, which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
- the class provides a method called `distance_from_point(point)`, which calculates the distance (like the previous method), but the other point's location is given as another Point class object;

Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

**Expected output**
```
1.4142135623730951
1.4142135623730951
```

### Lab [3.4.1.15](https://github.com/vionaaindah/python-essentials/blob/main/module-7/3.4.1.15.py)

**Estimated time**

30-60 minutes

**Level of difficulty**

Medium

**Objectives**

- improving the student's skills in defining classes from scratch;
- using composition.

**Scenario**

Now we're going to embed the `Point` class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called `Triangle` and this is the list of our expectations:

- the constructor accepts three arguments - all of them are objects of the Point class;
- the points are stored inside the object as a private list;
- the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)

Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Below you can copy the Point class code we used in the previous lab:
```
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y
```

**Expected output**
```
3.414213562373095
```
