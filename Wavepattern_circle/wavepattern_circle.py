import numpy as np
import cv2
import math

img = cv2.imread("C:\\01.jpg")
pixels = np.zeros_like(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
size = img.shape

for i in range(0, size[0]):
    for j in range(0, size[1]):
        pixels[i, j] = 255/2 + 255/2*math.sin(((j - size[1]/2)**2 + (i - size[0]/2)**2)**(1/2)/80*2*math.pi)

pixels = cv2.cvtColor(pixels, cv2.COLOR_GRAY2BGR)

layer = np.zeros_like(pixels)
layer[:, :, :] = np.array([255, 0, 255]).astype("uint8")

mixed = cv2. addWeighted(pixels, 0.8, layer, 0.2, 0)

final = cv2.addWeighted(img, 0.8, mixed, 0.3, 0)
cv2.imwrite("hello.jpg", final)