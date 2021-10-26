def checkPrisoners( t, i ):
    x = set( t.items() )
    y = set( i.items() )
    return x.issubset( y )