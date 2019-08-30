from math import cos,sin,pi

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



def trigo(x,y):
	if len(x)%2 == 0 :
		return nPar(x,y)
	else:
		return nImpar(x,y)


#x = [2*pi/3,4*pi/3,2*pi]
#y = [1,7,10]

#x = [0,pi/2,pi,3*pi/2]
#y = [1,3,-2,1]

x = [-2*pi/5,0,2*pi/5,4*pi/5,6*pi/5]
y = [1,1,0,-1,-2]


print(trigo(x,y))