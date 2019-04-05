import cv2
import numpy as np

img = cv2.imread('H:\\CroCon\\mains\\Assets\\images\\circle.png')
# resizing
dim = (int(img.shape[1] / 2), int(img.shape[0] / 2))
resize = cv2.resize(img, dim)
# -----------
gray_image = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
M = cv2.moments(thresh)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv2.circle(resize, (cX, cY), 5, (0, 0, 255), -1)
cv2.putText(resize, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
cv2.imshow("Image", resize)
cv2.waitKey(0) & 0xFF == ord('q')
cv2.destroyAllWindows()
