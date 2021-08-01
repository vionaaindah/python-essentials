class WeekDayError(Exception):
    pass
	

class Weeker:
    # Write code here
    __weekdays = ['Mon','Tus','Wed', 'Thu','Fri','Sat', 'Sun']

    def __init__(self, day):
        # Write code here
        try:
            self.__stat = self.__weekdays.index(day)
        except:
            raise WeekDayError

    def __str__(self):
        # Write code here
        return self.__weekdays[self.__stat]

    def add_days(self, n):
        # Write code here
        self.__stat = (self.__stat + n ) % 7

    def subtract_days(self, n):
        # Write code here
         self.__stat = (self.__stat - n ) % 7


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
