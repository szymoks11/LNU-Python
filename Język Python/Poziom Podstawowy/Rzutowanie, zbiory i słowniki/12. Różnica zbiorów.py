def getCustomers( myBase, theirBase ):
    nowa_baza = set(myBase)
    nowa_baza_konkurencji = set(theirBase)
    return nowa_baza_konkurencji-nowa_baza