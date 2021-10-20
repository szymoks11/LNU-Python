def add6months( date ):
    dot = date.index(".")
    rok = date[:dot]
    miesiac = date[dot+1:]
    if int(miesiac) > 6:
        int(rok) +=1
        int(miesiac) = int((miesiac) + 6) % 12
    elif int(miesiac) < 6:
        int(miesiac)+=6
    elif int(miesiac) < 4:
        miesiac = '0' + miesiac
    return str(rok)+"."+str(miesiac)