def decrypt( message, key):
    nowa = ""
    for x in message:
        nowa += chr( ord(x) // key )
    return nowa