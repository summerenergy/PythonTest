from PIL import Image
import cv2
import numpy as np
from pylab import *
img=Image.open('C:/Users/Administrator/Desktop/num2.jpg')
new_img = img.convert('L')
threshold  =   90
table  =  []
for  i  in  range( 256 ):
      if  i  <  threshold:
         table.append(1)
      else :
         table.append( 0 )

 #  convert to binary image by the table 
bim  =  new_img.point(table,'1')
tim=array(bim)
print(tim)
for i in range(5152):
   for j in range(2896):
      if i>4000 and j<1000:
         tim[i][j]=False

imshow(tim,cmap='binary')
show()

