"""使い方：インタープリターで１行ずつ実行して確認 """
import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))  # N-dimentional array

# 算術演算
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y

# shape形状（次元）が異なる場合、エラーが発生
a = np.array([1, 2, 3])  # shape (3,)
c = np.array([1, 2])  # shape (2,)
"""
a + c
Traceback (most recent call last):
  File "C:/Program Files/JetBrains/・・・/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (3,) (2,) 
"""
# ただし、下記の場合は、broadcastという機能によって、演算が可能になる
b = np.array([[4], [5], [6]])  # shape (3, 1)
# bの形状が(3, 1)に調整され、要素ごとの加算が可能
a + b
"""
array([[5, 6, 7],
       [6, 7, 8],
       [7, 8, 9]])
"""
x - y
