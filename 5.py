import numpy as np
import matplotlib.pyplot as plt

def mse(X, Y, mean_x, mean_y):
    return np.sqrt((X - mean_x) ** 2 + (Y - mean_y) ** 2)


x = np.random.randint(395, size=10)
y = np.random.randint(8232, size=10)
a = np.mean(x)
b = np.mean(y)

X, Y = np.meshgrid(x, y)

Z = mse(X, Y, a, b)

fig = plt.figure(figsize=(110, 60))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, np.log1p(Z), cmap='viridis')
ax2.set_title('MSE в логарифмической шкале по оси z')

plt.show()