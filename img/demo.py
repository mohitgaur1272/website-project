import cv2
img = cv2.imread('user.jpg')
resize_image = cv2.resize(img, (100, 100))
cv2.imwrite('user2.jpg',resize_image)



