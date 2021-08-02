from os import strerror
import os

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    # Write your code here.
    def __init__(self):
        Exception.__init__(self)
        print("Bad line of data in file !")
        exit()

class FileEmpty(StudentsDataException):
    # Write your code here.
    def __init__(self):
        Exception.__init__(self)
        print("Empty file offered !")
        exit()

def read_file(filename):
    with open(filename, 'rt') as file:
        lines = file.readlines()
        if len(lines) == 0:
            raise FileEmpty
        line_list = [line.split() for line in lines]
        dict = {}
        for text in line_list:
            if len(text) != 3:
                raise BadLine
            name = text[0] + ' ' + text[1]
            grade = float(text[2])
            if name in dict.keys():
                dict[name] += grade
            else:
                dict[name] = grade
    return dict

try:
    filename = input("Enter the source file name: ")
    dict = read_file(filename)
    list = sorted(dict.items(), key=lambda x: x[0])
    for name, point in list:
        print(name, '\t', point)

except BaseException as e:
    if(os.path.getsize(filename) == 0):
        raise FileEmpty()

    if(e == IOError):
        print("I/O error occurred: ", strerror(e.errno))

    if(e == ValueError):
        print("Value error")

    else:
        print("Unexpected error", strerror(e.errno))
