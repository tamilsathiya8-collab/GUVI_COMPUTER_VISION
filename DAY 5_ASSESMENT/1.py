import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("download.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

M = np.float32([[1,0,50],[0,1,50]])
translated = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

#2D ROTATION
M = cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 45, 1)
Rotated = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

#3D PRESPECTIVE TRANSFORMATION
pts1 = np.float32([[50,50],[200,50],[50,200],[200,200]])
pts2 = np.float32([[10,100],[200,50],[100,200],[220,220]])
M = cv2.getPerspectiveTransform(pts1,pts2)
prespective = cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))

#SHOW RESULTS

titles =["Original","translated","Rotated","prespective"]
images = [img,translated,Rotated,prespective]

for i in range(4):
    
    plt.subplot(2,2,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.axis("off")
    
plt.show()    