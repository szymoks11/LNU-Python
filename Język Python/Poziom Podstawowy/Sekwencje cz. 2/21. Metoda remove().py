def delNumber( t1, t2 ):
    for x in str(t2):
        print(t2)
        while t2 in t1:
            t1.remove( t2 )
    return t1