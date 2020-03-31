from Reconhecimento.app.Reconhecimento import Reconhecimento
from Treinamento.app.Treinamento import Treinamento

treinar = Treinamento("C:\\Users\\Vinicius Leal\\Desktop\\API\\Treinamento\\app\\ia\\shape.dat",
                "C:\\Users\\Vinicius Leal\\Desktop\\API\\Treinamento\\app\\ia\\dlib_face.dat",
                "C:\\Users\\Vinicius Leal\\Desktop\\API\\Treinamento\\app\\imagens de treinamento",
                "*.jpg")

treinar.treino()


#a = Reconhecimento("ia/shape.dat","ia/dlib_face.dat","recursos/img","C:/Users/Vinicius Leal/Desktop/API/2020-03-12_11.42.13.png","indices_rn_vini.pickel","descritores_rn_vini.npy")
#a.Reconhecer()

