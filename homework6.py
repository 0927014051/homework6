import numpy as np
import matplotlib.pyplot as plt

def read_data(data_path, size):
  with open(data_path, 'rb') as file:
    data = np.fromfile(file, dtype=np.uint8, count=size * size)
    return np.reshape(data, (size, size))

def show_image( x,x1, x2, x3, name):
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.imshow(x2, cmap='gray', vmin=0, vmax=255)
    plt.axis('image')
    plt.axis('off')
    plt.title(f"({name})", fontsize=12)

    plt.subplot(2, 2, 2)
    plt.imshow(x, cmap='gray', vmin=0, vmax=255)
    plt.axis('image')
    plt.axis('off')
    plt.title(f"3x3 Median Filter ({name})", fontsize=12)

    plt.subplot(2, 2, 3)
    plt.imshow(x1, cmap='gray', vmin=0, vmax=255)
    plt.axis('image')
    plt.axis('off')
    plt.title(f"3x3 Morphological Opening ({name})", fontsize=12)

    plt.subplot(2, 2, 4)
    plt.imshow(x3, cmap='gray', vmin=0, vmax=255)
    plt.axis('image')
    plt.axis('off')
    plt.title(f"3x3 Morphological Closing ({name})", fontsize=12)
    plt.show()

def filtersAndDisplay(input_file, size, wd_size, name):
    wd_size1 = wd_size // 2
    W = np.zeros((wd_size, wd_size))
    Y = np.zeros((size, size))
    Y1 = np.zeros((size, size))
    Y2 = np.zeros((size, size))
    y3 = np.zeros((size, size))
    Y4 = np.zeros((size, size))
    read = read_data(input_file, size)
    for row in range(wd_size1, size - wd_size1):
        for col in range(wd_size1, size - wd_size1):
            W = read[row - wd_size1:row + wd_size1 + 1, col - wd_size1:col + wd_size1 + 1]
            Y[row, col] = np.median(W)
            Y1[row, col] = np.min(W)
            Y4[row, col] = np.max(W)
    for row in range(wd_size1 + 1, size - wd_size1 - 1):
        for col in range(wd_size1 + 1, size - wd_size1 - 1):
            W = Y1[row - wd_size1:row + wd_size1 + 1, col - wd_size1:col + wd_size1 + 1]
            Y2[row, col] = np.max(W)
            W = Y4[row - wd_size1:row + wd_size1 + 1, col - wd_size1:col + wd_size1 + 1]
            y3[row, col] = np.min(W)
    show_image(read, Y, Y2, y3, name)
filtersAndDisplay("dataset/camera99.sec", 256, 3, 'camera99')
filtersAndDisplay("dataset/camera9.sec", 256, 3, 'camera9')
