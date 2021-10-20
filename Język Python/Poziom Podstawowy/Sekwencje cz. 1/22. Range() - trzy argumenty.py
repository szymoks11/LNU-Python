def reverse(s):
    rev = ""
    x = ""
    for x in range( len(s), 0, -1 ):
        rev += s[x-1]
    return rev