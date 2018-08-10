import dlib
import cv2
import numpy as np

def PrintPoint(IMG, pontosFaciais):
    for p in pontosFaciais.parts():
        cv2.circle(IMG, (p.x, p.y), 1, (255,255,0), 1)

def printLines(IMG, pontosFaciais):
    p68 = [[0, 16, False], # linha do queixo
           [17, 21, False], # sombrancelha direita
           [22, 26, False], # sombancelha esquerda
           [27, 30, False], # ponte nasal
           [30, 35, True], # nariz inferior
           [36, 41, True], # olho esquerdo
           [42, 47, True], # olho direito
           [48, 59, True], # labio externo
           [60, 67, True]] # labio interno
    for k in range(0, len(p68)):
        pontos = []
        for i in range(p68[k][0], p68[k][1] + 1):
            ponto = [pontosFaciais.part(i).x, pontosFaciais.part(i).y]
            pontos.append(ponto)
        pontos = np.array(pontos, dtype=np.int32)
        cv2.polylines(IMG, [pontos], p68[k][2], (255, 0, 0), 2)

FONT = cv2.FONT_HERSHEY_COMPLEX_SMALL
IMG = cv2.imread('fotos/treinamento/ronald.0.0.jpg')
DetectFace = dlib.get_frontal_face_detector()
DetectPoint = dlib.shape_predictor("Recursos/shape_predictor_68_face_landmarks.dat")
FaceDtect = DetectFace(IMG, 2)

for face in FaceDtect:
    pontos = DetectPoint(IMG, face)
    print(pontos.parts())
    PrintPoint(IMG, pontos)

cv2.imshow('Pontos faciais', IMG)
cv2.waitKey(0)
cv2.destroyAllWindows()