import cv2
import dlib

IMG = cv2.imread('IMG_T/GRUP.jpg')
Detect = dlib.get_frontal_face_detector()
FacesDetect = Detect(IMG)
print("FACES DETECTADAS: ", len(FacesDetect))

for Face in FacesDetect:
    e, t, d, b = int(Face.left()), int(Face.top()), int(Face.right()), int(Face.bottom())
    cv2.rectangle(IMG, (e,t), (d,b), (0,255,255), 2)

cv2.imshow("Detect hog", IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()