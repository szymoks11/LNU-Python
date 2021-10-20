def add6months(date):
    dot = date.index(".")
    rok = date[:dot]
    miesiac = date[dot + 1:]
    final_miesiac = int(miesiac)
    final_rok = int(rok)
    if final_miesiac > 6:
        final_rok += 1
        final_miesiac = (final_miesiac + 6) % 12
    elif final_miesiac == 6:
        final_miesiac += 6
    elif final_miesiac < 6:
        final_miesiac += 6
    if final_miesiac < 10:
        final_miesiac = '0' + str(final_miesiac)
        if final_miesiac == "00":
            final_miesiac == final_miesiac.replace("00", "12")
    return str(final_rok) + "." + str(final_miesiac)