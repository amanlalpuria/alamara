import numpy as np
import cv2
import imutils
import argparse
from matplotlib import pyplot as plt


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
image = imutils.resize(image, width=min(400, image.shape[1]))

gray = cv2.cvtColor(image,cv2.cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow("test", image)
cv2.waitKey(0)