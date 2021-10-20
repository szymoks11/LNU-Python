def saveScore( scores, hit ):
    doby_index= hit-1
    scores[doby_index] +=1
    return scores