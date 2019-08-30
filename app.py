from flask import Flask, request
import json

from zero_funcao import bisecao, posFalsa, newton_raphson, secante #Metodos de Zero da Função]
from zero_funcao import gravar #Metodos para gravar a função

from interpolacao import lagrange, polinomio_newton, spline, trigonometrica

from coef_correlacao import pearson, spearman, kendall




app = Flask(__name__)
@app.route('/', methods=['GET'])
def hello():
	return 'hello'


'''
Funções esperadas são todas da biblioteca Math do python, portanto digite-as conforme a documentação da biblioteca

'''

'''
Exemplo de input esperado:
{
	"a": "-100", 
	"b": "80",
	"error": "0.01",
	"f(x)": "x**3 - 2" 
}
'''
@app.route('/bisecao', methods=['POST'])
def bisecao_exe():
	a = request.json['a']
	b = request.json['b']
	error = request.json['error']
	formula = request.json['f(x)']
	
	gravar(formula)

	return bisecao(float(a),float(b),float(error))



'''
Exemplo de input esperado:
{
	"a": "-100", 
	"b": "80",
	"error": "0.01",
	"f(x)": "x**3 - 2" 
}
'''
@app.route('/posfalsa', methods=['POST'])
def posfalsa_exe():
	a = request.json['a']
	b = request.json['b']
	error = request.json['error']
	formula = request.json['f(x)']
	
	gravar(formula)

	return posFalsa(float(a),float(b),float(error))



'''
Exemplo de input esperado:
{
	"x": "100", 
	"error": "0.01",
	"f(x)": "x**2 - 2", 
	"fl(x)": "2*x"
}
'''
@app.route('/newton_raphson', methods=['POST'])
def newton_raphson_exe():
	x = request.json['x']
	error = request.json['error']
	formula = request.json['f(x)']
	lformula = request.json['fl(x)']
	
	gravar(formula,lformula)

	return newton_raphson(float(x),float(error))


'''
Exemplo de input esperado:
{
	"x0": "-100", 
	"x1": "80",
	"error": "0.01",
	"f(x)": "x**3 - 2" 
}
'''
@app.route('/secante', methods=['POST'])
def secante_exe():
	x0 = request.json['x0']
	x1 = request.json['x1']
	error = request.json['error']
	formula = request.json['f(x)']
	
	gravar(formula)

	return secante(float(x0),float(x1),float(error))


'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/lagrange', methods=['POST'])
def lagrange_exe():
	x = request.json['x']
	y = request.json['y']

	return lagrange(x,y)


'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/polinomio_newton', methods=['POST'])
def polinomio_newton_exe():
	x = request.json['x']
	y = request.json['y']

	return polinomio_newton(x,y)


'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/spline', methods=['POST'])
def spline_exe():
	x = request.json['x']
	y = request.json['y']

	return spline(x,y)



'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/trigonometrica', methods=['POST'])
def trigonometrica_exe():
	x = request.json['x']
	y = request.json['y']

	return trigonometrica(x,y)



'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/pearson', methods=['POST'])
def pearson_exe():
	x = request.json['x']
	y = request.json['y']

	return pearson(x,y)



'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/spearman', methods=['POST'])
def spearman_exe():
	x = request.json['x']
	y = request.json['y']

	return spearman(x,y)



'''
Exemplo de input esperado:
{
	"x": "1,2,3,4,5,6", 
	"y": "2,4,6,8,10,12",
}
'''
@app.route('/kendall', methods=['POST'])
def kendall_exe():
	x = request.json['x']
	y = request.json['y']

	return kendall(x,y)


if __name__ == '__main__':
	app.run()