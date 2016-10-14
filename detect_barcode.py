#import required packages for detect_barcode.py
import numpy as np
import argparse
import cv2

#construct the argument parse and parse the argument
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", requied = True, help = "/jurassic_world.jpg")
#args = vars(ap.parse_args)


#load the image and aconvert into the gray scale image
image = cv2.imread("jurassic_world.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#compute the scharr gradient magnitude representation of the images
#in both x and y cordiation
gradeX = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 1, dy = 0, ksize = -1)
gradeY = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 0, dy = 1, ksize = -1)

#substract the y-gradient from x- gradient
gradient = cv2.subtract(gradeX, gradeY)
gradient = cv2.convertScaleAbs(gradient)

#blur and threshold  the image
bluurred =cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(bluurred, 225, 255, cv2.THRESH_BINARY)

# construct a closing kernel and apply it to  the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21,7))
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

#perform a series of erosion and dialtion
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)

# find the contours in the thresholded image, then sort the contours
# by their area, keeping only the largest one
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.cv.BoxPoints(rect))
# draw a bounding box arounded the detected barcode and display the
# image
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)
