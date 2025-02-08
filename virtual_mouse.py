import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

# Camera setup
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Click debounce settings
last_click_time = 0
click_cooldown = 0.5  # 0.5 seconds cooldown

# Smoothing factor
smoothing_factor = 5
prev_x, prev_y = 0, 0

# Distance calculation
def calculate_distance(p1, p2):
    return math.hypot(p1.x - p2.x, p1.y - p2.y)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Cursor movement based on index finger
            index_finger = hand_landmarks.landmark[8]
            screen_x = int(index_finger.x * screen_width)
            screen_y = int(index_finger.y * screen_height)

            # Apply smoothing
            curr_x = prev_x + (screen_x - prev_x) / smoothing_factor
            curr_y = prev_y + (screen_y - prev_y) / smoothing_factor
            pyautogui.moveTo(curr_x, curr_y)

            prev_x, prev_y = curr_x, curr_y

            # Pinch gesture for click
            thumb_finger = hand_landmarks.landmark[4]
            distance = calculate_distance(thumb_finger, index_finger)

            # Dynamic threshold based on hand size
            wrist = hand_landmarks.landmark[0]
            middle_finger_tip = hand_landmarks.landmark[12]
            hand_size = calculate_distance(wrist, middle_finger_tip)
            click_threshold = hand_size * 0.3  # Adjust multiplier if needed

            # Click with debounce
            current_time = time.time()
            if distance < click_threshold and (current_time - last_click_time) > click_cooldown:
                pyautogui.click()
                last_click_time = current_time

    cv2.imshow("Hand-Controlled Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
