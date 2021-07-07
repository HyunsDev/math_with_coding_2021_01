import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim((0,2))
ax.set_ylim((-2,2))
ax.grid(True)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data(([],[]))
    return (line,)

def animate(t):
    x = np.linspace(0,2,1000)
    y= np.sin(2*np.pi*(x)*0.1*t)

    line.set_data(x,y)

    return (line,)

ani = animation.FuncAnimation(fig=fig, func=animate, init_func=init, interval=20, blit=True)

plt.show()