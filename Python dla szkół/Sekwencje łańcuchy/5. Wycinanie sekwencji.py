def get_year( year ):
    if year[0] == "_":
        return year[1:5]
    else:
        return year[0:4]
