def maxTemp(x):
    m = 0
    for y in x:
        if max( y ) > m:
            m = max( y )
    return m