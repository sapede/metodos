from pol import pol

x_ = [-1,0,1,2,3]
y_ = [1,1,0,-1,-2]

def func(x,y):
	S = pol([x[1],-1]).mulNum(y[0]/(x[1]-x[0])) + pol([-x[0],1]).mulNum(y[1]/(x[1]-x[0]))
	return S

def spline(x_data, y_data):
	x_copy = x_data[:]
	y_copy = y_data[:]

	splines = []

	for i in range(len(x_copy)-1):
		splines.append(func(x_copy[i:i+2],y_copy[i:i+2]))

	return list(zip(splines,x_copy,y_copy))
