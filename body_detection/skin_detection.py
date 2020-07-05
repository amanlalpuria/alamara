from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
image = imutils.resize(image, width=min(400, image.shape[1]))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)


# Convert YCbCr color space  - for skin detection
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([235,173,127],np.uint8)

image_YCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
skinRegionYCrCb = cv2.inRange(image_YCrCb,min_YCrCb,max_YCrCb)
skinYCrCb = cv2.bitwise_and(image, image, mask = skinRegionYCrCb)

cv2.imwrite("../img/ycrcb.png", np.hstack([image,skinYCrCb]))

# Convert HSV color space  - for hairs
image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# show the output image
# cv2.imshow("Image image_YCrCb", image_YCrCb)
cv2.imshow("Image skinRegionYCrCb", skinRegionYCrCb)
cv2.imshow("Image skinYCrCb", skinYCrCb)


cv2.waitKey(0)
cv2.destroyAllWindows()

