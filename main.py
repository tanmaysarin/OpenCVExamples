import cv2

# 0 for grayscale
# 1 for colored images
img = cv2.imread('lena.jpg', 1)

# drawing a line on the image
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()