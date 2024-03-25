import cv2
from cvzone.HandTrackingModule import HandDetector

# Load the image
image = cv2.imread('BME3/minhduc_frames/frame_0001.jpg')

# Initialize HandDetector
detector = HandDetector(maxHands=4)

# Padding to extend the crop area around the detected hand
padding = 20

# Detect hands and retrieve frame with annotations
hands, annotated_frame = detector.findHands(image, flipType=False)

if hands:
    # Get details of the first detected hand
    hand = hands[0]
    x, y, w, h = hand['bbox']

    # Calculate the dimensions for cropping
    x1, y1 = max(0, x - padding), max(0, y - padding)
    x2, y2 = min(image.shape[1], x + w + padding), min(image.shape[0], y + h + padding)

    # Crop the image and display if dimensions are valid
    crop = image[y1:y2, x1:x2]
    if crop.shape[0] > 0 and crop.shape[1] > 0:
        cv2.imshow('Cropped Image', crop)

# Display the annotated frame with hand detection results
cv2.imshow("Frame with Annotations", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
