import numpy as np
import matplotlib

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib import animation

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
"""
plt.plot(t,x)
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('x  y')
plt.legend(('x','y'))
plt.savefig('vanderpol.png')
"""
#animation support
fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.show()
def anim_init():
    l.set_data([], [])
    return l,

def animate(i):
	for index,ele in enumerate(solution):
		l.set_data(t[index], ele[0])

anim = animation.FuncAnimation(fig, animate, init_func=anim_init,
                               frames=200, interval=20, blit=False)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

metadata = dict(title='Vanderpol', artist='130010051', comment='Vanderpol evolution')

    


