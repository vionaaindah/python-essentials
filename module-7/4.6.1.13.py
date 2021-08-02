import calendar 

class MyCalendar:
    def __init__(self):
        self.__list = []
        self.__counter = 0
        self.__calendar = calendar.Calendar()

    def count_weekday_in_year(self, year, weekday):
         for i in range(12):
              for data in self.__calendar.monthdays2calendar(year, i+1):
                  self.__list += data
         for item in list:
              if item[0] != 0:
                  if item[1] == weekday:
                      self.__counter += 1
         return self.__counter 

year = int(input("Enter a year: "))
weekday = int(input("Enter a weekday (0-6) 0 is Monday: "))

cal = MyCalendar()
print(cal.count_weekday_in_year(year, weekday))
