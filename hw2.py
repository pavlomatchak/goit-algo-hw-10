import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

a = -1
b = 1

y_min = 0
y_max = 5

def func(x):
  return x ** 2 + x + 3

def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
  x = np.random.uniform(a, b, num_points)
  y = np.random.uniform(y_min, y_max, num_points)
  under_curve = np.sum(y < func(x))
  area = (b - a) * (y_max - y_min) * (under_curve / num_points)
  return area

x = np.linspace(a, b, 100)
y = func(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.axhline(y=y_min, color='k', linestyle="--")
ax.axhline(y=y_max, color='k', linestyle="--")
ax.axvline(x=a, color='k', linestyle="--")
ax.axvline(x=b, color='k', linestyle="--")

fill_x = np.linspace(a, b, 100)
fill_y = func(fill_x)
ax.fill_between(fill_x, fill_y, color='yellow', alpha=0.5)

plt.grid(True)
plt.show()

if __name__ == "__main__":
  result, err = integrate.quad(func, a, b)
  mc_result = monte_carlo_integrate(func, a, b, y_min, y_max, 1_000)
  print(f"Quad: {result: <.3f}")
  print(f"Monte Carlo: {mc_result: <.3f}")
