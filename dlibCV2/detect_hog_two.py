import cv2
import dlib

def Detecção(localimg, level):

    subDetect = ["Olhar a frente", "Vista a esquerda", "Vista a direita",
                 "A frente girando a esquerda", "A frente girando a direita"]

    IMG = cv2.imread(localimg)
    Detect = dlib.get_frontal_face_detector()
    FacesDetect, point, idx = Detect.run(IMG,level)

    for i,d in enumerate(FacesDetect):
        print("Detecção: {}, pontuação: {}, Sub-Detector: {}".format(d, point[i], subDetect[idx[i]]))
        e, t, d ,b = int(d.left()), int(d.top()), int(d.right()), int(d.bottom())
        cv2.rectangle(IMG, (e,t), (d,b), (0,255,255), 2)

    cv2.imshow("Detect hog", IMG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Detecção('IMG_T/ARENA.jpg',4)