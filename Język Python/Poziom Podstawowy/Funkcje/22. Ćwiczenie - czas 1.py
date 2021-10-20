def to_time(sec):
    if 0<=sec<=86000:
         return (sec//3600)*10000+(((sec%3600)//60) * 100 +(sec%3600)%60)