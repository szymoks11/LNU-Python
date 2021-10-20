def clearText( s ):
    new = ""
    for x in s:
        if x.isalnum():
            new += x
    return new