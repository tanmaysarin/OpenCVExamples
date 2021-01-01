import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) #returns a tuple of number of rows, columns and channels
print(img.size) # returns the total number of pixels accessed
print(img.dtype) # returns Image datatype

b, g, r = cv2.split(img)
print((b, g, r))
img = cv2.merge((b, g, r))

# copy a section of image to some other location
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# resize he two images to add them
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# add the images
dst = cv2.add(img, img2)

cv2.imshow('image', dst)
# cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()