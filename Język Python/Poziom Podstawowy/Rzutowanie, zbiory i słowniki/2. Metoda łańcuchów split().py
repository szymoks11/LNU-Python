def selectAndSum( x ):
    s= 0
    for y in x.split(', '):
        if y.isnumeric():
            s += int(y) 
    return s