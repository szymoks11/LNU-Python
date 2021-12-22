def countChars( s ):
    d = dict.fromkeys( s.upper() )
    for x in d:
        d[ x ] = s.upper().count( x )
    return d