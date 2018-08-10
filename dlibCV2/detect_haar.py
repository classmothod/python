import cv2

IMG = cv2.imread('IMG_T/GRUP.jpg')
classify = cv2.CascadeClassifier("Recursos/haarcascade_frontalface_default.xml")
imgCinza = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
facesDetect = classify.detectMultiScale(imgCinza, scaleFactor=1.4)
print(facesDetect)
print("Faces detectadas: ", len(facesDetect))
for (x,y,l,a) in facesDetect:
    cv2.rectangle(IMG, (x,y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow("Detector haar",IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()