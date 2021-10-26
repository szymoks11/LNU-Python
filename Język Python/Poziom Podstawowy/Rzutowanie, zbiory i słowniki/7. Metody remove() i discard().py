def clearData( x, y ):
    i = 0
    new = x.copy()
    for i in x:
        if int(i[1]) > int(y):
            new.remove(i)
    return new