from datetime import datetime, date
import cv2
import os

def img():
    tempo = datetime.now()
    camera = cv2.VideoCapture(0)
    id_imagem = str(date.today()) + '_' + str(tempo.hour) + '.' + str(tempo.minute) + '.' + str(tempo.second)
    PATH_IMAGE = os.path.join(os.getcwd(), 'Reconhecimento', 'app', 'img-regist', id_imagem+'.png')

    reva, img = camera.read()
    cv2.imwrite(PATH_IMAGE, img)
    print(PATH_IMAGE)
    return PATH_IMAGE