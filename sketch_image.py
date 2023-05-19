

# NAME : VAISHNAVI MAHENDRA BABAR.
# INTERNSHIP BY LetsGrowMore
# TASK 2 :- IMAGE TO SKETCH CONVERTING
# Beginner level program 


# To perform Any Image related task we need to import "cv2" Python library
# to use "cv2" library first of all we need to install "opencv-python" package by pip install ....

import cv2
img=cv2.imread('D:\shinchann.jpg')
cv2.imshow('Original image',img)   # imshow() Function will show the output image
cv2.waitKey(0)  # waitKey(0) function use to hold the output screen for long time .
# GRAY_IMAGE
gr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray_Scale Image', gr)
#cv2.waitKey(0)


# Invert Image
invert = cv2.bitwise_not(gr) # Using bitwise_not to invert the image
cv2.imshow('Inverted Image', invert)
cv2.waitKey(0)


# BLUR IMAGE
blur=cv2.GaussianBlur(invert,(21,21),0)
cv2.imshow('blur image', blur)
cv2.waitKey(0)


# INVERTED_BLUR IMAGE
invertBlur=255-blur
cv2.imshow('Inverted Blur', invertBlur)
cv2.waitKey(0)


#BLUR IMAGE
sketch=cv2.divide(gr,invertBlur,scale=256.0)
cv2.imshow('Sketch Image', sketch)
cv2.waitKey(0)

