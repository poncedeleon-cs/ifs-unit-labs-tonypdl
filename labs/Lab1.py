# Name:
# Period:
# Date:
    
# define a function leapYear() that takes a given year as
# a parameter and returns true if the given year is a leap
# year and false if the given year is not a leap year.

def leapYear(year):
    # Check if the year is divisible by 400, or divisible by 4 but not by 100
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

    



print(leapYear(1804))
print(leapYear(99))
print(leapYear(400))
print(leapYear(4000))
print(leapYear(4004))
print(leapYear(2200))
print(leapYear(1900))
print(leapYear(1906))
print(leapYear(1924))
print(leapYear(2112))
print(leapYear(1997))
