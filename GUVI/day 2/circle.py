import cv2
import matplotlib.pyplot as plt


img = cv2.imread("11.jpg")


cv2.circle(img, (50, 50), 50, (255, 0, 0), 2)


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img_rgb)
plt.axis("off")
plt.show()
