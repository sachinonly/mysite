#python3.9 -m pip install opencv-python
#or py -3.9 -m pip install opencv-python
# import cv2
#
# im_g = cv2.imread("C:\\Users\\sachin-windows\\Heloworld\\files\\smallgrey.png",0)
# print(im_g)
import os
import cv2
import numpy as np
#im_g = cv2.imread('C:\\Users\\sachin-windows\\Heloworld\\files\\smallgray.png',1)
# cv2.imwrite('C:\\Users\\sachin-windows\\Heloworld\\files\\newsmallgray.png', im_g)
#Below Can Convert also from png to jpg
im_god = cv2.imread('C:\\Users\\sachin-windows\\Heloworld\\files\\smallgray.png',1)
cv2.imwrite('C:\\Users\\sachin-windows\\Heloworld\\files\\newsmallgray.png', im_god)

print(im_god)
print("Transposed ************")
for i in im_god.T:
    print(i)
print("Flat One by One Value ************")
for i in im_god.flat:
    print(i)