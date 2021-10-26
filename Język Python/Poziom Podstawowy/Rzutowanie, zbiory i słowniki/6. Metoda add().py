def setSet( x ):
    lista = []
    i = 0
    for loginy in x:
        lista.append(x[i][0])
        i+= 1
    posortowane = set(lista)
    return posortowane