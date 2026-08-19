import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Maruthi\Downloads\METAL.jpg")

kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

sharp=cv2.filter2D(img,-1,kernel)

cv2.imshow("Original",img)
cv2.imshow("Sharpened",sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
