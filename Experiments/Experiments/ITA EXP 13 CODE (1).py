import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    rows,cols=frame.shape[:2]

    pts1=np.float32([[50,50],[cols-50,50],[50,rows-50],[cols-50,rows-50]])
    pts2=np.float32([[0,100],[cols,0],[100,rows],[cols-100,rows]])

    M=cv2.getPerspectiveTransform(pts1,pts2)
    dst=cv2.warpPerspective(frame,M,(cols,rows))

    cv2.imshow("Original",frame)
    cv2.imshow("Perspective Video",dst)

    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
