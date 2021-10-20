def maxPeriod( debt, equity ):
    lata = 0
    while debt < equity:
        lata = lata+1
        debt *= 1.035
    return lata