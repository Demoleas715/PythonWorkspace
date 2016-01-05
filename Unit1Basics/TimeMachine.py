'''
Created on Oct 19, 2015

@author: Evan
'''
DAY_OF_WEEK = ("Sunday", "Monday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def is_leap_year(year):
    if year%400==0:
        return True
    
    elif (year%4==0) and (year%100!=0):
        return True
    
    else:
        return False
    
def get_days_in_month(month, year):    
    if (month in (1, 3, 5, 7, 8, 10, 12)):
        days = 31
    elif (month in (4, 6, 9, 11)):
        days=30
    elif month==2:
        if is_leap_year(year):
            days=29
    
        else:
            days=28
    else:
        print("Month is invalid: " + str(month))
        
    return days
    
def get_days_in_months(start_month, end_month, year):
    total=0
    
    for m in range (start_month, end_month):
        total+=get_days_in_month(m, year)
    
    return total

def get_days_in_years(start_year, end_year):
    total = 0
    
    for y in range (start_year, end_year):
        if (is_leap_year(y)):
            total+=366
        else:
            total+=365
            
    return total
            
def get_day_of_week (day, month, year):
    total=get_days_in_years(1004, year)
    total+= get_days_in_months(1, month, year)
    total+=day-1
    
    total%=7
    
    return DAY_OF_WEEK[total]
    
def main():
    year=int(input("Time traveler - What year do you want to go to?"))
    month=int(input("Time traveler - What month do you want to go to?"))
    day=int(input("Time traveler - What day would you like to go to?"))
    
    dayString=get_day_of_week(day, month, year)
    
    print("By my calculations, the day will be %s" % (dayString))
    
main()