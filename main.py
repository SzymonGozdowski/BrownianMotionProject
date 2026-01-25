import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

fig, (ax1, ax2) = plt.subplots(1, 2)

xdata, ydata = [], []

ln1, = ax1.plot([], [], 'ro')
ln2, = ax2.plot([], [], 'g-')

ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)

# --- SLIDERY ---

# time step slider
ax_slider_time = plt.axes((0.2, 0.05, 0.6, 0.02))
slider_time = Slider(ax_slider_time, "Time step [ms]", 1, 1000, valinit=800)

# r scale slider
ax_slider_r = plt.axes((0.2, 0.01, 0.6, 0.02))
slider_r = Slider(ax_slider_r, "r scale", 0.01, 5.0, valinit=1.0)

def init():
    return ln1, ln2

def update(frame):
    r = slider_r.val * np.random.randn()
    alpha = np.random.uniform(-2*np.pi, 2*np.pi)

    xdata.append(r * np.cos(alpha))
    ydata.append(r * np.sin(alpha))

    ln1.set_data(xdata, ydata)
    ln2.set_data(xdata, ydata)
    return ln1, ln2

ani = FuncAnimation(
    fig,
    update,
    frames=1000,
    init_func=init,
    interval=slider_time.val,
    blit=False
)

def on_time_change(val):
    ani.event_source.interval = val

slider_time.on_changed(on_time_change)

plt.show()
