def isPalindrom(x):
    y = x.copy()
    x.reverse()
    if x == y:
        return True
    else:
        return False