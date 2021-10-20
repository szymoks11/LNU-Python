def findLongest( x ):
    i = ""
    m = 0
    for i in x:
        if len( i ) > m:
            m = len( i )
    return m