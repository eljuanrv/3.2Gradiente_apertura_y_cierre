#RIVERA VARGAS JUAN
import numpy as np
import cv2
from matplotlib import pyplot as plt

#Cargar la mascara
imagen = cv2.imread('runner2.jpeg',0)
imagen0 = cv2.imread('runner2.jpeg',0)
#Crear un kernel de &#39;1&#39; de 3x3
kernel = np.ones((2,2),np.uint8)
#Se aplica la transformacion: Closing
transformacion = cv2.morphologyEx(imagen,cv2.MORPH_CLOSE,kernel)
#Mostrar el resultado y salir
_, imagen = cv2.threshold(transformacion, 160, 255, cv2.THRESH_BINARY)
imagen = cv2.bitwise_not(imagen)


kernel = np.ones((4,4),np.uint8)
transformacion = cv2.dilate(imagen,kernel,iterations = 4)
transformacion = cv2.morphologyEx(transformacion,cv2.MORPH_OPEN,kernel)
transformacion = cv2.morphologyEx(transformacion,cv2.MORPH_CLOSE,kernel)
transformacion = cv2.erode(transformacion,kernel,iterations = 2)

transformacion = cv2.bitwise_not(transformacion)



titles = ['Original','Solido']
images = [imagen0,transformacion]
miArray = np.arange(2)
for i in miArray:
  plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()
