def countGarfield( names ):
    lista = []
    for e in names:
            lista.append(e)
    if "Garfield" in lista:
        return lista.index("Garfield")+1
print(countGarfield(iter( [ 'Tom', 'Garfield', 'Azrael' ] )))