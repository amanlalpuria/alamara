import cv2
import numpy as np
from openpose import pyopenpose as op

params = {
    "model_folder": "./models/",
    "face": False,
    "hand": False
}
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

image_path = "img\test_4.JPG"
image = cv2.imread(image_path)
datum = op.Datum()
datum.cvInputData = image
opWrapper.emplaceAndPop([datum])

# Extract keypoints
keypoints = datum.poseKeypoints

# Calculate measurements
def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

shoulder_width = calculate_distance(keypoints[0][2], keypoints[0][5])
waist_size = calculate_distance(keypoints[0][8], keypoints[0][11])
height = calculate_distance(keypoints[0][1], keypoints[0][8])

print(f"Shoulder Width: {shoulder_width}")
print(f"Waist Size: {waist_size}")
print(f"Height: {height}")
