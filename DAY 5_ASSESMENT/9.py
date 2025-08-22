#Brute_Force_Matching
import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread('download.jpg')
img2 = cv2.imread('download.jpg')

#ORB Keypoint Extractor
orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)

Brute_force = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
match = Brute_force.match(des1, des2)

matches = sorted(match,key=lambda x: x.distance)

result = cv2.drawMatches(img1,kp1,img2,kp2, match[:30],None, flags=0)

plt.imshow(cv2.cvtColor(result,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()