def testA( t1, t2 ):
    lista1 = []
    lista2 = []
    for e in t1:
        lista1.append(e)
        
        print(lista1)
        x = lista1.count("a")
        L1 = tuple(lista1)
    for a in t2:
        lista2.append(a)
        print(lista2)
        y = lista2.count("a")
        L2 = tuple(lista2)
    if x>y:
        return L1 + L2
    if y>x:
        return L2 + L1
    elif x == y:
        return L1 + L2