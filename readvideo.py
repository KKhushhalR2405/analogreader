import cv2 
import imutils
import numpy as np
import math
#from skimage.transform import (hough_line, hough_line_peaks)

img=cv2.imread("analog.jpg",0)
#roi=img[80:500 , 0:600]
#cv2.imshow("ROI",roi)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100)
output=img.copy()
"""edged = c.Canny(img, 30, 150)
c.imshow("Edged", edged)"""
if circles is not None:
	
	circles = np.round(circles[0, :]).astype("int")
 
	
	for (x, y, r) in circles:
		
		cv2.circle(output, (x, y), r, (0, 0, 255), 4)
		
 
	#edged = cv2.Canny(output, 30, 150)
	#cv2.imshow("Edged", edged)
	cv2.imshow("output", output)  
	cv2.waitKey(0)

edges = cv2.Canny(img, 75, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 55,maxLineGap=250)
print(lines)
angle=[]
for line in lines:
   x1, y1, x2, y2 = line[0]
   angle.append(math.atan((y2-y1)/(x2-x1)))
   cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 1)

   cv2.imshow("ofo",img)
   cv2.waitKey(0)
#cv2.imshow("linesEdges", edges)
#cv2.waitKey(0)
angled=[]
for i in angle:
	angled.append(math.degrees(i))
print(angle)
print(angled)
cv2.imshow("linesDetected", img)
cv2.waitKey(0)
a1=angled[0]
a2=angled[2]
a3=180-(a2-a1)
print(a3)

#dgdfgfgdfg


"""image=img.copy()

# Compute arithmetic mean
image = np.mean(image, axis=2)

# Perform Hough Transformation to detect lines
hspace, angles, distances = hough_line(image)

# Find angle
angle=[]
for _, a , distances in zip(*hough_line_peaks(hspace, angles, distances)):
    angle.append(a)

# Obtain angle for each line
angles = [a*180/np.pi for a in angle]

# Compute difference between the two lines
angle_difference = np.max(angles) - np.min(angles)
print(angle_difference)"""