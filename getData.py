from PIL import Image
import os, glob

import numpy as np
from sklearn import model_selection
from tqdm import tqdm

classLabels = ["monkey", "boar", "crow"]
image_size = 50

# 画像の読み込み
X = []
Y = []

for index, classLabel in enumerate(tqdm(classLabels)):
    photos_dir = "image/" + classLabel
    fileLabels = glob.glob(photos_dir + "/*.jpg")

    for i, fileLabel in enumerate(fileLabels):
        if i >= 200 : break
        image = Image.open(fileLabel)
        image = image.convert("RGB") # 数値へ変換
        image = image.resize((image_size, image_size)) # サイズを揃える
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
Y = np.array(Y)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y)

# np.savezを使用して複数の配列を保存
np.savez("./animal.npz", X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)