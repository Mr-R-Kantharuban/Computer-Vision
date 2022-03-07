import cv2

path = r'C:\Users\User\OneDrive\Documents\cv\bharathiyar.jpg'
input=cv2.imread(path)
cv2.imshow('image',input)
cv2.waitKey()
cv2.destroyAllWindows()