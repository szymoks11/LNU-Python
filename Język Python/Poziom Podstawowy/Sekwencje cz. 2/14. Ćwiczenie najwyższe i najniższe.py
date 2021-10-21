def highLow( t1, t2 ):
    duzaLista = t1+t2
    duzaLista.sort(reverse = True)    
    return duzaLista[:3]+duzaLista[-3:]