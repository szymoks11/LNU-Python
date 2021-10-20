def setPower( pm25, pm10 ):
    if pm25>36 or pm10>80:
        return 3
    elif pm25>= 25 or pm10 >= 51:
        return 2  
    elif pm25>=13 or pm10>=21:
        return 1
    elif pm25 <12 or pm10 <20:
        return 0
