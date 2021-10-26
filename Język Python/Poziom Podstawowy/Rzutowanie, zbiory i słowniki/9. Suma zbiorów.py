def getEmails( s1, s2 ):
    lista = []
    i = 0
    x = 0
    for zgoda in s1:
        if s1[i][1] == True:
            lista.append(s1[i][0])
        i+= 1
    for zgoda in s2:
        if s2[x][1] == True:
            lista.append(s2[x][0])
        x+= 1
    return set(lista)