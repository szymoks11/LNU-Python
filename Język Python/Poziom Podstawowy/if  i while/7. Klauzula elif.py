#your code

def dayOfWeek(x):
    if x == 1:
        value =  "Monday"
    if x == 2:
        value =  "Tuesday"
    elif x == 3:
        value =  "Wednesday"
    elif x == 4:
        value =  "Thursday"
    elif x == 5:
        value =  "Friday"
    elif x == 6:
        value =  "Saturday"
    elif x == 7:
        value =  "Sunday"
    if x > 8:
        value = "wrong value"
    return value