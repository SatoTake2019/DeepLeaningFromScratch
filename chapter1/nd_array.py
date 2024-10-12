"""使い方：インタープリターで１行ずつ実行して確認 """
import numpy as np

A = np.array([[1, 2], [3, 4]])
print(A)

A.shape
# (2, 2)   # ２×２の行列ということ
A.dtype
# dtype('int64')  # 要素のデータ型は64bit整数

# 行列の和
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
A + B
"""
array([[ 4,  2],
       [ 3, 10]])
"""
A * B   # 要素同士の積
"""
array([[ 3,  0],
       [ 0, 24]])
"""
A @ B   # 行列の積
"""
array([[ 3, 12],
       [ 9, 24]])
"""









# 行列のスカラー演算（和・差・積・商）
2 + A
"""
array([[3, 4],
       [5, 6]])
"""
A + 2
"""
array([[3, 4],
       [5, 6]])
"""
2 - A
"""
array([[ 1,  0],
       [-1, -2]])
"""
A - 2
"""
array([[-1,  0],
       [ 1,  2]])
"""
2 * A
"""
array([[2, 4],
       [6, 8]])
"""
A * 2
"""
array([[2, 4],
       [6, 8]])
"""
2 / A
"""
array([[2.        , 1.        ],
       [0.66666667, 0.5       ]])
"""
A / 2
"""
array([[0.5, 1. ],
       [1.5, 2. ]])
"""
