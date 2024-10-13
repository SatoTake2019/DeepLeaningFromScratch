import numpy as np
import matplotlib.pylab as plt


def relu_function(x: np.ndarray) -> np.ndarray:
    """ReLU(Restricted Linear Unit) function"""
    return np.maximum(0, x)


x = np.arange(start=-5.0, stop=5.0, step=0.1)
y = relu_function(x)

# 軸の範囲と目盛りを指定
plt.plot(x, y)
plt.ylim(-1, 5.3)
plt.xlim(-6, 6)

plt.show()
