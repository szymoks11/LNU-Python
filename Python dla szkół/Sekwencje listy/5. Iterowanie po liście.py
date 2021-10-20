def formatNames( names ):
    dlugosc_list = len(names)
    nowa_lista = []
    for x in range(dlugosc_list):
        nowa_lista.append("Mr. "+names[ x ])
    return nowa_lista