from pol import *

x = [2,3,4,7,8]
y = [-3,8,21,1.4,1]


def newton(x,y):
    dTemp = y[:]
    d = []
    d.append(y[0])
    for j in range(1,len(x)):
        lista = []
        cont = 0
        for i in range(0,len(x)-j):
            var = (dTemp[cont+1]-dTemp[cont])/(x[i+j]-x[i])
            cont +=1
            lista.append(var)
        dTemp = lista[:]
        d.append(dTemp[0])


    p = pol()

    for i in range(len(d)):
        pTemp = pol([d[i]])
        for j in range(0,i):
            pTemp *= pol([-x[j],1])
        p += pTemp

    return p


print(newton(x,y))