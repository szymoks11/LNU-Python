def findLongest(x):
    max_length = len(x[0])
    longest_string = x[0]
    for y in x:
        if len( y ) > max_length:
            max_length = len(y)
            longest_string = y
    return longest_string
