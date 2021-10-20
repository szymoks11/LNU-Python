def oddChars(s):
    y = ""
    for x in range(1,len(s),2):
        y += s[x]
    return y