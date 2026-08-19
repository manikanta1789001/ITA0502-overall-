import cv2

image = cv2.imread(r"C:\Users\Maruthi\Downloads\TREE.jpg")

if image is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Original Image", image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
