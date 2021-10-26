def sumUp( data, nr ):
    total = 0
    for x in data:
        if x[0] == nr:
            total += x[1]
    return total