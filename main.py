import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, (ax1, ax2) = plt.subplots(1, 2)
xdata, ydata = [], []
ln1, = ax1.plot([], [], 'ro')
ln2, = ax2.plot([], [], 'g-')

def init():
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)
    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-10, 10)
    return ln1, ln2

def update(frame):
    if frame != 0:
        r = np.random.randn()
        alpha = np.random.uniform(-2*np.pi, 2*np.pi)
        xdata.append(r * np.cos(alpha))
        ydata.append(r * np.sin(alpha))
        """
        xdata.append(xdata[frame -1] + np.random.uniform(-0.5, 0.5))
        ydata.append(ydata[frame -1] + np.random.uniform(-0.5, 0.5))
        """
    ln1.set_data(xdata, ydata)
    ln2.set_data(xdata, ydata)
    return ln1, ln2


xdata.append(int(input("Podaj x0: ")))
ydata.append(int(input("Podaj y0: ")))


ani1 = FuncAnimation(fig, update, frames=100,
                    init_func=init, blit=True)

plt.show()