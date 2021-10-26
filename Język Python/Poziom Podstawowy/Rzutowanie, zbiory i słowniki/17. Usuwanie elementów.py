import time
def update(x):
    t= 20161024
    y = dict( x )
    i= 0 
    for i in x:
        if int(x[i][1]) < t:
            del y[ i ]
    return y