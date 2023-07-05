'''
A year may be a leap year if it is evenly divisible by 4.
Years that are divisible by 100 (century years such as 1900 or 2000) cannot be leap years
unless they are also divisible by 400. (For this reason, the years 1700, 1800,
and 1900 were not leap years, but the years 1600 and 2000 were.)
'''

year = (input('enter a year :'))

#to take elements from last of the list use -1 -2 -3 and so on...

if year[-1]=='0' and year[-2]=='0' :
    year=int(year)
    if year % 400 ==0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    
else:
    year=int(year)
    if year%4==0:
        print(f"{year} is a leap year")
    else:
        print('it is not a leap year')

