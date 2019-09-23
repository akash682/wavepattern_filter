import numpy as np
import cv2
import math

img = cv2.imread("C:\\01.jpg")
pixels = np.zeros_like(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
size = img.shape

for i in range(0, size[0]):
    for j in range(0, size[1]):
       pixels[i, j] = 255/2*math.sin(i*math.pi/100) + 255/2

pixels = cv2.cvtColor(pixels, cv2.COLOR_GRAY2BGR)

mixed = cv2.addWeighted(img, 0.9, pixels, 0.3, 0)
final = cv2.addWeighted(img, 0.2, mixed, 0.8, 0)

cv2.imwrite("hello.jpg", final)