import os

def find(path, dir):
  list = [x[0] for x in os.walk(path)]
  list = sorted(list, key=len)

  for directory in list:
    if directory.endswith(dir):
        print(".." + directory)

path = input("Enter the source path name: ")
dir = input("Enter the source dir name: ")

print()
find(path, dir)
