from pol import *
from math import cos,sin,pi
from zero_funcao import convert_json


def converte_string(string):
    lista = string.replace(' ', '')
    lista = lista.split(',')
    lista = [float(n) for n in lista]
    return lista


def lagrange(a,b):
    x = converte_string(a)
    y = converte_string(b)
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

    return convert_json('f(x)', temp)


def polinomio_newton(a,b):
    x = converte_string(a)
    y = converte_string(b)
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

    return convert_json('f(x)', p)

def retornoSpline(x,splines):
    x2 = x[1:]
    x1= x[:-1]
    return  convert_json('((intervalo),spline)',list(zip(x1,x2,splines)))


def funcSpline(x,y):
    S = pol([x[1],-1]).mulNum(y[0]/(x[1]-x[0])) + pol([-x[0],1]).mulNum(y[1]/(x[1]-x[0]))
    return S

def spline(a, b):
    x = converte_string(a)
    y = converte_string(b)

    splines = []

    for i in range(len(x)-1):
        splines.append(funcSpline(x[i:i+2],y[i:i+2]))

    strSplines = [str(s) for s in splines]
    return retornoSpline(x,strSplines)



def nImpar(x_data,y_data):

    x = x_data[:]
    y = y_data[:]

    n = int((len(x_data)))
    m = int((n-1)/2)

    A = []
    B = []
    for j in range(m+1):
        tempA = 0
        tempB = 0
        for k in range(n):
            tempA += y[k]*cos(j*x[k])
            tempB += y[k]*sin(j*x[k])

        A.append(2/n*tempA)
        B.append(2/n*tempB)

    func = ''

    func += str(A[0]/2) + ' '

    for k in range(1,m+1):
        ind1 = (' + ' + str(A[k])) if A[k]>=0 else (' - ' + str(A[k]*-1))
        ind2 = (' + ' + str(B[k])) if B[k]>=0 else (' - ' + str(B[k]*-1))
        func +=  (ind1 + '*cos(' + str(k) + '*x)' + ind2 + '*sen(' + str(k) + '*x)')

    return func


def nPar(x_data,y_data):
    x = x_data[:]
    y = y_data[:]

    n = int((len(x_data)))
    m = int((n)/2)

    A = []
    B = []
    for j in range(m+1):
        tempA = 0
        tempB = 0
        for k in range(n):
            tempA += y[k]*cos(j*x[k])
            tempB += y[k]*sin(j*x[k])

        A.append(2/n*tempA)
        B.append(2/n*tempB)

    func = ''

    func += str(A[0]/2) + ' '

    for k in range(1,m):
        func += (' + ' + str(A[k]) + '*cos(' + str(k) + '*x) + ' + str(B[k]) + '*sen(' + str(k) + '*x) ')

    func += ' + ' + str(A[m]/2) + '*cos(' + str(m) + '*x)'
    return func



def trigonometrica(a,b):
    x = converte_string(a)
    y = converte_string(b)
    if len(x)%2 == 0 :
        return convert_json('f(x)',nPar(x,y))
    else:
        return convert_json('f(x)',nImpar(x,y))
