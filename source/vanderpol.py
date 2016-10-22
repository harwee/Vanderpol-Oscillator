import numpy as np
import matplotlib
import os

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
	line1.set_ydata(np.ma.array(t, mask=True))
	line2.set_ydata(np.ma.array(t, mask=True))
	return line1, line2,

if __name__ == "__main__":
	cur_path = list(os.path.split(os.getcwd()))
	out_path = cur_path[:-1]
	out_path.extend(['output'])
	out_path = os.path.join(*out_path)
	
	x0 = [1,2]
	t = np.linspace(0,100,1000)

	solution = odeint(vanderpol_func,x0,t)

	fig = plt.figure()
	ax = plt.axes(xlim=(np.amin(t), np.amax(t)+0.1), ylim=(np.amin(solution)-0.1, np.amax(solution)+0.1))

	line1, = ax.plot([],[], label="x")
	line2, = ax.plot([],[], label="y=dx/dt")
	plt.legend(handles=[line1, line2])
	plt.title('Van der Pol oscillator')
	plt.xlabel('time')
	plt.ylabel('Variation of x and dx/dt')

	x = solution[:,0]

	y = solution[:,1]
	
	ani = animation.FuncAnimation(fig, animate, np.arange(len(t)), init_func=init, blit=True)
	print(out_path)
	ani.save(os.path.join(out_path,'vanderpol_130010051.mp4'), fps=30, extra_args=['-vcodec', 'libx264'])
	fig.savefig(os.path.join(out_path,'vanderpol_130010051.png'))