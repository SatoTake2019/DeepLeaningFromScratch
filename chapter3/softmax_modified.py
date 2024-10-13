import numpy as np
import matplotlib.pylab as plt


def softmax_modified(a: np.ndarray) -> np.ndarray:
    """
    入力値の最大値を分子分母に掛けて、指数法則でexpの中にいれるという式の変形により、
    オーバーフローを起こさないようにした。
    """
    c = np.max(a)
    exp_a = np.exp(a - c)  # Overflow prevention
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([1010, 1000, 999])  # オーバーフローが起きなくなった
b = softmax_modified(a)
print(b)
#  [9.99937902e-01 4.53971105e-05 1.67006637e-05]
