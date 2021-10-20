def encrypt( message ):
    mask = ""
    for x in message:
        ord(x)
        mask += chr( ord(x) * 2 )

    return mask