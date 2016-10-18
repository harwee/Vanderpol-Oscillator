import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

def vanderpol_func(dim,t): 
	x, y = dim
	dxdt = y
	dydt = mu*(1.0-x*x)*y-x
	return [dxdt,dydt]