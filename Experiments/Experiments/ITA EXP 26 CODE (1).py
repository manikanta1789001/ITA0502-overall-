import cv2

img = cv2.imread(r"C:\Users\Maruthi\Downloads\CLIMATE.png")

watermark = img.copy()

cv2.putText(watermark,"MARUTHI",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow("Original",img)

cv2.imshow("Watermarked Image",watermark)

cv2.waitKey(0)

cv2.destroyAllWindows()
