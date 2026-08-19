import cv2

img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg",0)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

sobel=cv2.addWeighted(cv2.convertScaleAbs(sobelx),0.5,cv2.convertScaleAbs(sobely),0.5,0)

cv2.imshow("Original",img)
cv2.imshow("Sobel XY",sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()
