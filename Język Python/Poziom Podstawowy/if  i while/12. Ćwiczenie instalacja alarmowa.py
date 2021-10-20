#your code
def checkTriangle(pret1,pret2,pret3):
    if pret1<pret2+pret3 and pret2<pret1+pret3 and pret3<pret2+pret1 and pret3>pret2-pret1 and pret1>pret3-pret2 and pret2>pret3-pret1:
        return True
    else:
        return False
