def encrypt( message ):
    nowa = ""
    for x in range(len(message)):
        nowa += chr( ord( message[ x ] ) + x )
    return nowa