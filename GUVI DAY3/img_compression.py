import cv2


img = cv2.imread("image.jpeg")

cv2.imwrite("compressed_image_30.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),30])
cv2.imwrite("compressed_image_90.jpeg",img,[int(cv2.IMWRITE_JPEG_QUALITY),90])