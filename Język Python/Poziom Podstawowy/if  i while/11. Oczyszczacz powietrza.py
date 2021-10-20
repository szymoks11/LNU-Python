def setAlarm(h,d):
    if d in range(1,5) and h in range(6,22):
        return False
    elif d==5 and h in range(6,18):
        return False
    elif d==6 and h in range(6,14):
        return False
    else:
        return True