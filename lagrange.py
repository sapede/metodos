from pol import *

x = [2,3,4,7,8]
y = [-3,8,21,1.4,1]
def lagrange(x,y):
    L = []
    for n in range(len(x)):
        temp = pol([1])
        for i in range(len(x)):
            if i != n:
                temp *= pol([-x[i],1]).divNum(x[n]-x[i])
        L.append(temp)

    temp = pol()
    for i in range(len(L)):
        temp += L[i].mulNum(y[i])

    return temp


print(lagrange(x,y))