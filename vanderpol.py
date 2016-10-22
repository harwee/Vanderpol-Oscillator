import numpy as np
import matplotlib

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

def vanderpol_func(X,t): 
	mu = 1
	x, y = tuple(X)
	dxdt = y
	dydt = mu*(1.0-x*x)*y-x
	return [dxdt,dydt]

def animate(i):
	line1.set_data(t[:i],x[:i])
	line2.set_data(t[:i],y[:i])
	return line1, line2,

def init():
	line1, = ax.plot([],[])
	line2, = ax.plot([],[])
	line1.set_ydata(np.ma.array(t, mask=True))
	line2.set_ydata(np.ma.array(t, mask=True))
	return line1, line2,



if __name__ == "__main__":
	x0 = [1,2]
	t = np.linspace(0,100,1000)


	solution = odeint(vanderpol_func,x0,t)

	fig = plt.figure()
	ax = plt.axes(xlim=(np.amin(t), np.amax(t)+0.1), ylim=(np.amin(solution)-0.1, np.amax(solution)+0.1))


	x = solution[:,0]
	y = solution[:,1]

	ani = animation.FuncAnimation(fig, animate, np.arange(len(t)), init_func=init, blit=True)
	ani.save('vanderpol.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
