def bestStudent( studentScores ):
    i = 0
    lista = []
    oceny = []
    for e in studentScores:
        lista.append(e)
        oceny.append(e[1])
    oceny.sort(reverse= True)
    maksymalna = oceny[0]
    for name in lista:
        if name[1] == maksymalna:
            return name[0]