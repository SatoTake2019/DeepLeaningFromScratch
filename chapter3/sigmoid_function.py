import numpy as np
import matplotlib.pylab as plt


def sigmoid_function(x: np.ndarray) -> np.ndarray:
    """引数に ndarrayを取り、要素が float の ndarrayを返す"""
    return 1 / (1 + np.exp(-x))


# ステップ関数の入力データと同じで、要素数が100個、各要素の型がdtype('float64') の ndarray
x = np.arange(start=-5.0, stop=5.0, step=0.1)
print(x)
y = sigmoid_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
