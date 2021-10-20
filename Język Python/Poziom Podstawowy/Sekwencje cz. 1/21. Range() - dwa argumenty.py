def charsInDoc(a, b):
    s = 0
    for x in range( a, b + 1 ):
        s += charsOnPage( x )
    return s