import cv2
import numpy as np

# Initialize the QR Code detector
detector = cv2.QRCodeDetector()

# Start the webcam
cap = cv2.VideoCapture(0)

# Define the size and position for the green box
box_size = 200  # Size of the square box
box_center = (320, 240)  # Center position of the box (assuming 640x480 resolution)

print("Scanning for QR codes... Press 'q' to exit.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Draw a green square box on the frame
    top_left = (box_center[0] - box_size // 2, box_center[1] - box_size // 2)
    bottom_right = (box_center[0] + box_size // 2, box_center[1] + box_size // 2)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Use the detector's detectAndDecode method
    data, bbox, _ = detector.detectAndDecode(frame)

    # If a QR code is detected
    if data:
        # Draw the bounding box around the detected QR code
        if bbox is not None:
            # Ensure bbox has 4 points
            if bbox.shape[0] == 4:
                for i in range(4):
                    cv2.line(frame, tuple(bbox[i][0]), tuple(bbox[(i + 1) % 4][0]), (0, 255, 0), 3)

        # Display the "Detected" text on the frame
        cv2.putText(frame, "Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Print the decoded data
        print("QR Code detected:", data)

    # Display the frame with the drawn box and detected QR code
    cv2.imshow("QR Code Scanner", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
