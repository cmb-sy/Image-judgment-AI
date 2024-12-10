from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import numpy as np

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

def main():
    data = np.load("./animal.npy.npz", allow_pickle=True)
    X_train = data['X_train']
    X_test = data['X_test']
    y_train = data['y_train']
    y_test = data['y_test']

    X_train = X_train.astype("float") / 256
    X_test = X_test.astype("float") / 256

    # ワンホットエンコーディングに変換
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    print(X_train.shape)
    print(y_train.shape)

    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)

if __name__ == "__main__":
    main()