import numpy as np
import matplotlib.pylab as plt


def softmax_basic(a: np.ndarray) -> np.ndarray:
    """
    入力値を0から1の範囲に正規化し、全ての出力の合計が1になるようにしている
    """
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


a = np.array([0.3, 2.9, 4.0])   # 問題ない
b = softmax_basic(a)
print(b)

a = np.array([0.3, 2.9, 1000])
b = softmax_basic(a)
print(b)
"""
RuntimeWarning: invalid value encountered in divide
  y = exp_a / sum_exp_a
[ 0.  0. nan]
"""
