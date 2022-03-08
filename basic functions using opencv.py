import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)
path = r'C:\Users\User\OneDrive\Documents\cv\bharathiyar.jpg'
input=cv2.imread(path)
imagegray=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(input,(5,5),0)
imgcanny=cv2.Canny(input,100,100)
imgDilation=cv2.dilate(input,kernel,iterations=1)
imgEroded=cv2.erode(input,kernel,iterations=1)
cv2.imshow('image',input)
cv2.imshow('imagegray',imagegray)
cv2.imshow('image blur',imgblur)
cv2.imshow('imgcanny',imgcanny)
cv2.imshow('imgDilation',imgDilation)
cv2.imshow('imgEroded',imgEroded)
cv2.waitKey()
cv2.destroyAllWindows()