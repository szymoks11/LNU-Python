def convert( x ):
    y = x.copy()
    for index in range( len(y) ):
        if y[ index ] < 0:
            y[ index ] = 0
        elif y[ index ] > 10:
            y[ index ] = 10
    return x+y