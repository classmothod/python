import os
import glob
import _pickle as cPickle
import dlib
import cv2
import numpy as np

DetectFace = dlib.get_frontal_face_detector()
DetectPoint = dlib.shape_predictor("Recursos/shape_predictor_68_face_landmarks.dat")
ReconFacial = dlib.face_recognition_model_v1("Recursos/dlib_face_recognition_resnet_model_v1.dat")

Index = {}
IDX = 0
Descript = None

for arq in glob.glob(os.path.join("fotos/treinamento", "*.jpg")):
    IMG = cv2.imread(arq)
    FaceDetect = DetectFace(IMG, 1)
    NumberFace = len(FaceDetect)

    if NumberFace > 1 or NumberFace < 1:
        print("ERROR")
        exit(0)

    for face in FaceDetect:
        pontosFaciais = DetectPoint(IMG, face)
        DescriptFacial = ReconFacial.compute_face_descriptor(IMG, pontosFaciais)

        ListDescript = [df for df in DescriptFacial]
        npArray = np.asarray(ListDescript, dtype=np.float64)
        npArray = npArray[np.newaxis, :]

        if Descript is None:
            Descript = npArray
        else:
            Descript = np.concatenate((Descript, npArray), axis=0)

        Index[IDX] = arq
        IDX += 1

print("Tamanho: {} Formato: {}".format(len(Descript), Descript.shape))

    #cv2.imshow("Treinamento", IMG)
    #cv2.waitKey(0)
#cv2.destroyAllWindows()