import calendar
from datetime import datetime
# monday   = 0
# tuesday  = 1
# wednesday= 2
# thursday = 3
# friday   = 4
# saturday = 5
# sunday   = 6
anyday=int(input("enter day:"))
def saturdays_in_month(year, month):
    # get the number of days in the given month
    num_days = calendar.monthrange(year, month)[1]
    
    # check each day in the month
    saturdays = []
    for day in range(1, num_days + 1):
        # create a datetime object for the given day
        date = datetime(year, month, day)
        # if the day is a Saturday, add it to the list of saturdays
        
        if date.weekday() == anyday:
            saturdays.append(date.strftime('%Y-%m-%d'))
    
    return saturdays

saturdays = saturdays_in_month(2023, 3)
print(saturdays) 


# dynamic value for saturday