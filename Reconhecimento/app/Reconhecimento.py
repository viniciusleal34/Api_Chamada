# -*- coding: utf-8 -*-
import dlib
import cv2
import os
import datetime
import numpy as np
from datetime import datetime


class Reconhecimento:
    def __init__(self, detectorPontos, reconhecimentoFacial, caminho, img, indice, descritorFace, limiar = 0.55):
        self.cont = 0
        self.detectorFace = dlib.get_frontal_face_detector()
        self.detectorPontos =  dlib.shape_predictor(detectorPontos)
        self.reconhecimentoFacial = dlib.face_recognition_model_v1(reconhecimentoFacial)
        self.indice = np.load(indice)
        self.descritoresFaciais= np.load(descritorFace)
        self.limiar = limiar
        self.caminho = caminho
        self.img = img
        self.alunos = []



    def Reconhecer(self):
        
        imagem = cv2.imread(self.img)
        facesDetectadas = self.detectorFace(imagem,1)
        for face in facesDetectadas:
            e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
            pontosFaciais = self.detectorPontos(imagem, face)
            descritorFacial = self.reconhecimentoFacial.compute_face_descriptor(imagem, pontosFaciais)
            listaDescritorFacial = [fd for fd in descritorFacial]
            npArrayDescritorFacial = np.asarray(listaDescritorFacial, dtype=np.float64)
            npArrayDescritorFacial = npArrayDescritorFacial[np.newaxis, :]

            distancias = np.linalg.norm(npArrayDescritorFacial - self.descritoresFaciais, axis=1)
            minimo = np.argmin(distancias)
            distanciaMinima = distancias[minimo]

            if distanciaMinima <= self.limiar:
                tempo = datetime.now()
                codigo = os.path.split(self.indice[minimo])[1].split(".")[0]
                self.alunos.append(codigo)
            else:
                codigo = ' '
#'''
            cv2.rectangle(imagem, (e,t),(d,b),(0,255,255),2)
            texto = "{} {:.4f}".format(codigo, distanciaMinima)
            cv2.putText(imagem, texto, (d,t), cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,255,255))

        cv2.imshow("Detector", imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#'''
    def getAlunosPresentes(self):
        return self.alunos
