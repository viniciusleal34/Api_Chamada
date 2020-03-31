import cv2
from Reconhecimento.app.Reconhecimento import Reconhecimento
from datetime import datetime, date
from Reconhecimento.app.Registro import Registro
from Reconhecimento.app.Gerador_imagem import img
import time
import os

PATH_SHAPE = os.path.join(os.getcwd(),'Reconhecimento' ,'app', 'ia', 'shape.dat')
PATH_FACES = os.path.join(os.getcwd(),'Reconhecimento' ,'app', 'ia', 'dlib_face.dat')
PATH_IMG = os.path.join(os.getcwd(),'Reconhecimento' ,'app', 'img-regist')
PATH_INDICE = os.path.join(os.getcwd(),'Reconhecimento' ,'app', 'indices')
PATH_DESCRITOR = os.path.join(os.getcwd(),'Reconhecimento' ,'app', 'descritores')

def main(args):
    while True:
        tempo = datetime.now()
        a = Reconhecimento(
            PATH_SHAPE,
            PATH_FACES,
            PATH_IMG,
            img(),
            PATH_INDICE+"\\indices_rn_vini.pickel",
            PATH_DESCRITOR+"\\descritores_rn_vini.npy"
        )
        a.Reconhecer()
        for nome in a.getAlunosPresentes():
            registro = Registro(str(nome), tempo.date(), tempo.hour, tempo.minute)
        time.sleep(600)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))





