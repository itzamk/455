# Andrew Kozempel
# CMPSC 497
# Lab 5

import cv2
import numpy as np

# Your camera initialization
camera_pipeline = "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink"
camera = cv2.VideoCapture(camera_pipeline, cv2.CAP_GSTREAMER)

# This loop is here since the first few frames taken by the camera are dark.
for i in range(100):
    __, frame = camera.read()

# Function to find red objects
def find_red_objects(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return None
    largest_contour = max(contours, key=cv2.contourArea)
    moments = cv2.moments(largest_contour)
    if moments["m00"] == 0:
        return None
    cx = int(moments["m10"] / moments["m00"])
    cy = int(moments["m01"] / moments["m00"])
    return cx, cy

# Main loop to check for red objects and control the robot
while True:
    ret, frame = camera.read()
    if not ret:
        break

    red_object_center = find_red_objects(frame)

    if red_object_center:
        # If red object is detected, move towards it
        robot_move_forward()
    else:
        # Otherwise, keep spinning to search for red object
        robot_spin()

# Cleanup
camera.release()
