import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

def legendre_poly(x, degree):
    return legendre(degree)(x)


x = np.linspace(-1, 1, 1000)
degrees = [1, 2, 3, 4, 5, 6, 7]

plt.figure(figsize=(12, 12))
plt.title('Полиномы Лежандра')

for degree in degrees:
    y = legendre_poly(x, degree)
    plt.plot(x, y, label=f"n = {degree}")
plt.legend()
plt.grid(True)
plt.show()