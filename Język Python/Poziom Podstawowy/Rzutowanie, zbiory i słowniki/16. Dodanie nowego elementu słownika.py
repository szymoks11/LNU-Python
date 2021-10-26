def convert( x ):
    y = dict()
    for i in x:
        y[ str( i ) ] = x[ i ]
    return y