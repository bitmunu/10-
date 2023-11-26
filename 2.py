import numpy as np
from numpy import sin,pi
import matplotlib.pyplot as plt
m = [[3, 2], [3, 4], [5, 4], [5, 6]]
plt.figure(1)

for i in m:         
         a = i[0]
         b = i[1]
         d = 0.5 * pi
         x = [sin(a*t + d) for t in np.arange(0, 2*pi, 0.01)]
         y = [sin(b*t) for t in np.arange(0, 2*pi, 0.01)]

         if m.index(i) == 0:
                  plt.subplot(221)
                  plt.plot(x, y, 'black')
                  plt.grid(True)

         elif m.index(i) == 1:
                  plt.subplot(222)
                  plt.plot(x, y, 'black')
                  plt.grid(True)

         elif m.index(i) == 2:
                  plt.subplot(223)
                  plt.plot(x, y, 'black')
                  plt.grid(True)
         else:
                  plt.subplot(224)
                  plt.plot(x, y, 'black')
                  plt.grid(True)
plt.show()