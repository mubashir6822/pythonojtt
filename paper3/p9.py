def leapyear(year):

    if (year % 400 == 0) and (year % 100 == 0):
        return(f"{year} is a leap year")

    elif (year % 4 ==0) and (year % 100 != 0):
        return(f"{year} is a leap year")
    else:
        return("{0} is not a leap year".format(year))\
        
print(leapyear(int(input('enter a year : '))))