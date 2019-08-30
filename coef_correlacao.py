import json
from zero_funcao import convert_json
from interpolacao import converte_string

def pearson(x_data, y_data):
    x = converte_string(x_data)
    y = converte_string(y_data)

    n = len(x)

    xl = sum(x)/n
    yl = sum(y)/n

    somaX = 0
    somaY = 0
    somaP = 0

    for i in range(n):
        tempX = x[i]-xl
        tempY = y[i]-yl

        somaP += tempY*tempX
        somaX += tempX**2
        somaY += tempY**2

    r = somaP/(somaX**0.5 * somaY**0.5)

    return convert_json('r', r)


def spearman(x_data, y_data):
    x_dados = converte_string(x_data)
    y_dados = converte_string(y_data)

    x_ord = sorted(x_dados)
    y_ord = sorted(y_dados)

    n = len(x_dados)

    somaD2 = 0
    for x,y in zip(x_dados,y_dados):
        somaD2 += (x_ord.index(x) - y_ord.index(y))**2

    p = 1 - (6*somaD2)/(n*(n**2 - 1))

    return convert_json('p', p)


def kendall(x_data, y_data):
    x = converte_string(x_data)
    y = converte_string(y_data)

    concordantes = 0
    discordantes = 0

    n = len(x)

    for i in range(n-1):
        for j in range(i+1,n):
            if (x[j] > x[i] and y[j] > y[i]) or (x[j] < x[i] and y[j] < y[i]):
                concordantes += 1
            else:
                discordantes += 1

    r = (concordantes - discordantes)/(n*(n-1)/2)

    return convert_json('r',r)

