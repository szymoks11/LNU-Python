def avgRuntime( x ):
    space = x.index(" ")
    minuty = int(x[:space])
    odcinki = int(x[space+1:])
    return minuty / odcinki