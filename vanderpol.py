import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

mu = 1
def vanderpol_func(X,t): 
	x, y = tuple(X)
	dxdt = y
	dydt = mu*(1.0-x*x)*y-x
	return [dxdt,dydt]

x0 = [1,2]
t = np.linspace(0,100,1000)

solution = odeint(vanderpol_func,x0,t)

#adding plotting functions
x = [ele[0] for ele in solution]
y = [ele[1] for ele in solution]
plt.plot(t,x)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('x  y')
plt.legend(('x','y'))
plt.show()

