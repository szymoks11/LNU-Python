def clearUnderscore(s):
    lista_od_s = list(s)
    while True:
        if "_" in lista_od_s:
            lista_od_s.remove("_")
            continue
        return lista_od_s