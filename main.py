import cv2
import numpy as np

image = cv2.imread('img5.jpg')

# Resize the image for easier processing (optional)
image = cv2.resize(image, (800, 600))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        cv2.drawContours(image, [contour], -1, (0, 0, 255), 2)

# Display the result
cv2.imshow('Detected Cracks', image)
cv2.waitKey(0)
cv2.destroyAllWindows()