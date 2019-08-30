import func
import json
import os
import importlib



#Metodos para carregar a funcao no cache
def carregar():
    try:
        os.system('del /q c:\\Prog\\Met\\__pycache__\\func.cpython-37.pyc')
        importlib.reload(func)
    except:
        pass


#Metodo para gravar a função num arquivo
def gravar(formula :str, lformula='0'):
    arq2 = open("c:\\Prog\\Met\\func.py",'w')

    arq2.write('from math import *\n\n')
    arq2.write('def f(a):\n')
    arq2.write('    x = float(a)\n')
    arq2.write('    return '+ formula +'\n')

    arq2.write('\ndef fl(a):\n')
    arq2.write('    x = float(a)\n')
    arq2.write('    return '+ lformula +'\n')

    arq2.close()
    
    carregar()


#Converte uma chave e um conteudo em arquivo json
def convert_json(key, content):
    key = str(key)
    content = str(content)
    file_json = {key: content}
    return json.dumps(file_json, indent = 2)


#Função utilizada para calculr a Bisecção
def funBip(a,b):
    f = func.f
    x = (a+b)/2
    if(f(x)*f(b)<=0):
        return [x,b]
    elif(f(x)*f(a)<=0):
        return [x,a]
    else:
        return 0;
    

#Método da Bisecção, entradas são um valor de 'a' e 'b' para intervalo e o erro estipulado
def bisecao(a1,b1, err):
    f = func.f
    a = a1
    b = b1
    erro = err
    cont = 0
    try:
        while(cont<10000):
            cont+=1
            l = funBip(a,b)
            a = l[0]
            b = l[1]
            if(abs(f(l[0]))<erro):
                break
        return convert_json('x', a)
    except:
        raise Exception('O intervalo digitado não possui o zero da função')




#Função utilizada no calculo da Posição Falsa
def funPF(a,b):
    f = func.f
    x = (a*f(b)-b*f(a))/(f(b) -f(a))
    if f(x)*f(a)<=0:
        return [x,a]
    if f(x)*f(b)<=0:
        return [x,b]
    return 0


#Método da posição falsa, entradas são um valor de 'a' e 'b'' para intervalo e o erro estipulado
def posFalsa(a1,b1,erro):
    f = func.f
    a = a1
    b = b1
    cont = 0
    try:
        while(cont<1000000):
            cont+=1
            l = funPF(a,b)
            a = l[0]
            b = l[1]
            if(abs(f(l[0]))<erro):
                break
        return convert_json('x',a)
    except:
        raise Exception('O intervalo digitado não possui o zero da função')


#Função utilizada no calculo do newton_raphson
def funN(x):
    f = func.f
    fl = func.fl
    return x - f(x)/fl(x)


#Método de newton_raphson, entradas são um valor de 'a'  e o erro estipulado
def newton_raphson(a,erro):
    f = func.f
    x = a
    cont = 0
    while (abs(f(x))>=erro and cont<10000):
        cont+=1
        x = funN(x)
    return convert_json('x',x)


#Função utilizada no calculo da secante
def funSec(x1, x2):
    f = func.f
    return (x1*f(x2) - x2*f(x1))/(f(x2) - f(x1))


#Método de newton_raphson, entradas são um valor de 'a' e 'b' e o erro estipulado
def secante(a,b,erro):
    f = func.f
    x1 = a
    x2 = b
    cont = 0
    while(abs(f(x2))>=erro and cont<10000000):
        x1, x2 = x2, funSec(x1,x2)
        cont+=1
    return convert_json('x',x2)




