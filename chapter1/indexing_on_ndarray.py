"""使い方：インタープリターで１行ずつ実行して確認 """
import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
"""
[[51 55]
 [14 19]
 [ 0  4]]
"""
X[0]
"""
array([51, 55])
"""
X[0][1]
"""
np.int64(55)
"""
X[0, 1]  	# この方法は ndarray特有でリストにはない indexing方法
"""
np.int64(55)
"""
X[-1][-1]  # 負のインデックスもOK
# np.int64(4)


print(X[0, 1])
"""
55
"""
for row in X:
    print(row)
"""
[51 55]
[14 19]
[0 4]
"""
F = X.flatten()
print(F)
"""
[51 55 14 19  0  4]
"""

C = np.arange(start=0, stop=10, step=1)
