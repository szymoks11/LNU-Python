import time 
def displayTime():
    czas = time.ctime()
    dzien_tygodnia = czas[:3]
    godzina = czas[11:19]
    return godzina+" "+dzien_tygodnia.upper()