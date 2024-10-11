import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(start=0, stop=6, step=0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# グラフの描画
plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos", linestyle="--")
plt.xlabel("x")  # x軸ラベル
plt.ylabel("y")  # y軸ラベル
plt.title('sin & cos')
plt.legend()  # 凡例
plt.show()
