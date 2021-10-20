def everyThird( value ):
    y = ""
    for x in range(0,len(value),3):
        y = y + value[ x ]
    return y