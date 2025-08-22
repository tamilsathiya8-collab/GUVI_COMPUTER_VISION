import cv2
import matplotlib.pyplot as plt

img = cv2.imread("download.jpg")
print(img.shape)

cv2.rectangle(img,(150,100),(50,50),(0,0,255),3)


plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()