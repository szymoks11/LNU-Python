from datetime import date
def englishBreakfast(x):
    i = 0
    listy = [[]] * len(x)
    for dni in x:
        rok = x[i][1][:4]
        miesiac = x[i][1][4:6]
        dzien = x[i][1][6:]
        agent = x[i][0]
        d0 = date(int(rok), int(miesiac), int(dzien))
        d1 = date(2021, 10, 23)
        delta = d1 - d0
        x[i][1] = delta.days
        i+= 1
    return x