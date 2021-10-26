def brutto( x ):
    cena = x[:-1]
    cena_po_podwyzce = float(cena)/100*108
    cena_zaokraglona = round(cena_po_podwyzce, 2)
    return str(cena_zaokraglona)+" "+ x[-1]