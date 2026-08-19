import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg")

rows,cols=img.shape[:2]

pts1=np.float32([[50,50],[300,50],[50,300],[300,300]])
pts2=np.float32([[20,80],[280,40],[80,280],[320,320]])

H,_=cv2.findHomography(pts1,pts2)
dst=cv2.warpPerspective(img,H,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("Homography",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
