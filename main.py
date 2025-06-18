import cv2
from cvzone.HandTrackingModule import HandDetector
from keys import PressKey, ReleaseKey, space_pressed
import time

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
space_key_pressed = space_pressed
time.sleep(2.0)

# Key tracking set
current_key_pressed = set()

# Start webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Flip and resize
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800, 600))
    keyPressed = False
    key_count = 0
    key_pressed = 0

    # Detect hands
    hands, img = detector.findHands(frame)

    # Draw bottom UI panel
    overlay = img.copy()
    cv2.rectangle(overlay, (0, 530), (800, 600), (0, 0, 0), -1)
    alpha = 0.6
    img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    # UI text variables
    gesture_text = "No Hand Detected"
    jump_status = "Not Jumping"

    if hands:
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)

        # Draw finger circles
        for i, isUp in enumerate(fingerUp):
            centerX, centerY = lmList['lmList'][4 * (i + 1)][:2]
            color = (0, 255, 0) if isUp else (0, 0, 255)
            cv2.circle(img, (centerX, centerY), 20, color, -1)

        gesture_text = f"Finger Count: {sum(fingerUp)}"

        if fingerUp == [0, 0, 0, 0, 0]:
            jump_status = "Jumping"
            PressKey(space_key_pressed)
            current_key_pressed.add(space_key_pressed)
            keyPressed = True
            key_count += 1
            key_pressed = space_key_pressed
        else:
            jump_status = "Not Jumping"

        if not keyPressed and len(current_key_pressed) != 0:
            for key in current_key_pressed:
                ReleaseKey(key)
            current_key_pressed = set()
        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key != key_pressed:
                    ReleaseKey(key)
            current_key_pressed = set()

    # Draw text overlay
    cv2.putText(img, gesture_text, (20, 580), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(img, jump_status, (600, 580), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    # Show the frame
    cv2.imshow("Gesture Control Interface", img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
