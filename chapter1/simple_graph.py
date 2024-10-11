import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(start=0, stop=6, step=0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
plt.show()
