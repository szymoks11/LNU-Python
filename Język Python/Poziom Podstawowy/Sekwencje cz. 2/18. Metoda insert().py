def temperature(x):
    celc = x[0]
    F = celc*9/5+32
    x.insert( -1, F )
    return x