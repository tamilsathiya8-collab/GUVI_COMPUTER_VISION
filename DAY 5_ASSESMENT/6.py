import cv2
import matplotlib.pyplot as plt
img = cv2.imread("download.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.imshow(cv2.cvtColor(thresh,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()