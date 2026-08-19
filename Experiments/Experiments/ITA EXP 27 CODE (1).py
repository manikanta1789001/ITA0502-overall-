import cv2

img = cv2.imread(r"C:\Users\Maruthi\Downloads\CLIMATE.png")

h, w = img.shape[:2]

crop = img[20:h//2, 20:w//2]

crop = cv2.resize(crop, (100,100))

img[10:110, 10:110] = crop

cv2.imshow("Output", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
