import numpy as np
import time
from numpy import sin,pi
import matplotlib.pyplot as plt
plt.ion()
for pepega in np.arange(0, 1, 0.01):
    a = 3
    b = a * pepega
    x = [sin(a*t) for t in np.arange(0., 2*pi, 0.01)]
    y = [sin(b*t) for t in np.arange(0., 2*pi, 0.01)]

    plt.clf()

    plt.plot(x, y, 'black')
    plt.grid(True)

    plt.draw()
    plt.gcf().canvas.flush_events()

    plt.ioff()
plt.show()
