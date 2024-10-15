# coding: utf-8
import os
import sys
import numpy as np
from PIL import Image

# スクリプトが存在するディレクトリの親ディレクトリをパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from dataset.mnist import load_mnist


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

# 訓練画像、訓練ラベル   テスト画像、テストラベル
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 形状を元の画像サイズに変形
print(img.shape)  # (28, 28)

# pixchar = ".-~=:;^O08%&$W@#"
# pixchar = "米髟面鼎蠻鬣麌黌鬱䨻"
pixchar = "░▒▓█"

for i, pix in enumerate(x_train[0]):
    if pix != 0:
        print(f'{pixchar[pix // int(256 / len(pixchar))]}', end='')
    else:
        print('  ', end='')
    if i % 28 == 0:
        print()
