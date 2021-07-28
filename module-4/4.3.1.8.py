def is_year_leap(year):
# Your code from LAB 4.3.1.6.
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
  return False

def days_in_month(year, month):
# Your code from LAB 4.3.1.7.
  if month < 1 or month > 12:
    return None
  leap_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_year_leap(year) == True and month == 2:
    return 29
  return leap_month[month - 1]

def day_of_year(year, month, day):
# Write your new code here.
  if days_in_month(year, month) == None:
    return None
  total_days = 0
  for i in range(month - 1):
    total_days += days_in_month(year, i + 1)
  if day > days_in_month(year, month):
    return None
  return total_days + day

print(day_of_year(2000, 12, 31))
