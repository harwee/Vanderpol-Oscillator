import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


def vanderpol_func(X,t): 
	x, y = tuple(X)
	dxdt = y
	dydt = mu*(1.0-x*x)*y-x
	return [dxdt,dydt]

x0 = [1,2]
t = np.linspace(0,100,1000)

solution = odeint(vanderpol_func,x0,t)
