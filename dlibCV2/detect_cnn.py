import cv2
import dlib

def detecção(localimg):

    IMG = cv2.imread(localimg)
    Detect = dlib.cnn_face_detection_model_v1("Recursos/mmod_human_face_detector.dat")
    faceDetect = Detect(IMG,1)

    for face in faceDetect:
        e, t, d, b, c = (int(face.rect.left()), int(face.rect.top()), int(face.rect.right()), int(face.rect.bottom()), face.confidence)
        print(c)
        cv2.rectangle(IMG, (e,t), (d,b), (255,255,0), 2)

    cv2.imshow("Detector CNN", IMG)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detecção('IMG_T/ARENA.jpg')