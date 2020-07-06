import argparse
import imutils
import cv2
import skindetection as sd


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread(args["image"])
image = imutils.resize(image, width=min(400, image.shape[1]))

skinRegionYCrCb, image, skinYCrCb = sd.skin_detection(image)

# show the output image
# cv2.imshow("Image image_YCrCb", image_YCrCb)
cv2.imshow("Image skinRegionYCrCb", skinRegionYCrCb)
cv2.imshow("Image skinRegionYCrCb Contour", image)
cv2.imshow("Image skinYCrCb", skinYCrCb)


cv2.waitKey(0)
cv2.destroyAllWindows()