def findName( d, n ):
    for x in d:
        if x["NIP"] == n:
            return x["name"]
    else:
        return "Data not found"