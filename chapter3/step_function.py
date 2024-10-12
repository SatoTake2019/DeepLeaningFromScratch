import numpy as np
import matplotlib.pylab as plt


def step_function(x: np.ndarray) -> np.ndarray:
    return np.array(x > 0, dtype=np.int64)


x = np.arange(start=-5.0, stop=5.0, step=0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
