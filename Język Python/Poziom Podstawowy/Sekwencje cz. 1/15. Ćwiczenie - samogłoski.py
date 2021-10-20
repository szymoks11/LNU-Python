def maxOrd( text ):
    m = 0
    for x in text:
        if ord(x) > m:
                m = ord(x)
    return m