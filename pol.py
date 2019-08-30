class pol():
    """docstring for pol"""
    def __init__(self, lista = []):
        self.coefs = lista

    def __str__(self):
        string = ''
        tam = len(self.coefs)
        if tam == 0 or (tam == 1 and self.coefs[0] == 0):
            string = '0'
        else:
            if self.coefs[tam-1] != 0:
                string += str('%.3f'%self.coefs[tam-1]) + 'x^' +  str(tam-1)
            for i in range(tam-2,0,-1):
                if self.coefs[i] != 0:
                    if self.coefs[i] < 0:
                        string += ' - '
                    else:
                        string += ' + '

                    string += str('%.3f'%abs(self.coefs[i])) + 'x^' +  str(i)

            if self.coefs[0] != 0:
                if self.coefs[0] < 0:
                    string += ' - '
                else:
                    string += ' + '
                string += str('%.3f'%abs(self.coefs[0]))
        return string

    def __add__(self, outro):
        lista = []
        tam1 = len(self.coefs)
        tam2 = len(outro.coefs)
        for i in range(max(tam1,tam2)):
            if i<tam1 and i<tam2:
                lista.append(self.coefs[i]+outro.coefs[i])
            elif i<tam1:
                lista.append(self.coefs[i])
            elif i<tam2:
                lista.append(outro.coefs[i])
        return pol(lista)

    def __neg__(self):
        lista = [ -x for x in self.coefs]
        lista = pol(lista)
        return lista

    def __sub__(self, outro):
        return self + (-outro)

    def __mul__(self, outro):
        tam1 = len(self.coefs)
        tam2 = len(outro.coefs)

        temp = [0]* (tam1+tam2-1)
        p = pol()

        for i in range(tam1):
            lista = temp[:]
            for j in range(tam2):
                c = self.coefs[i]*outro.coefs[j]
                ind = i + j
                lista[ind] = c
            p += pol(lista)

        return p

    def mulNum(self, n):
        lista = [x*n for x in self.coefs]
        return pol(lista)

    def divNum(self, n):
        return self.mulNum(1/n)