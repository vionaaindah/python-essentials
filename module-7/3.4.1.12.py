class Timer:
    def __init__(self, hour, minute, second):
        # Write code here
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        # Write code here
        __second = self.__second
        __minute = self.__minute
        __hour = self.__hour
        if self.__second < 10:
            __second = '0' + str(self.__second)
        if self.__minute < 10:
            __minute = '0' + str(self.__minute)
        if self.__hour <10:
            __hour = '0' + str(self.__hour)        
        time = str(__hour) + ':' + str(__minute) + ':' + str(__second)
        return time

    def next_second(self):
        # Write code here
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def prev_second(self):
        # Write code here
        if self.__second == 0:
            self.__second = 59
            if self.__minute == 0:
                self.__minute = 59
                if self.__hour == 0:
                    self.__hour = 23
                else:
                    self.__hour -= 1
            else:
                self.__minute -= 1    
        else:
            self.second -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
