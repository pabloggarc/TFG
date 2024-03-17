import numpy as np
import cv2
from scipy import signal

X = np.array([[1, 2, 3, 4, 5], 
             [5, 6, 7, 8, 9], 
             [9, 8, 7, 6, 5], 
             [5, 4, 3, 2, 1],
             [1, 2, 3, 4, 5]])

K = np.array([[-1, 0, 1], 
             [-2, 0, 2], 
             [-1, 0, 1]])

conv = signal.convolve2d(X, K, mode = "valid")
print(conv)

X = X.astype(np.float32)
K = K.astype(np.float32)

conv = cv2.filter2D(X, -1, K, borderType = cv2.BORDER_CONSTANT)[1:-1, 1:-1]
print(conv)