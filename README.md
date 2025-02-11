# 🖱️ Hand-Controlled Virtual Mouse

This project is a **Hand-Controlled Virtual Mouse** powered by Python, OpenCV, MediaPipe, and PyAutoGUI. It enables users to control the mouse cursor and perform click actions using simple hand gestures via a webcam.

## 🚀 Features
- **Real-time Hand Tracking** using MediaPipe.
- **Smooth Cursor Movement** with jitter reduction.
- **Gesture-Based Clicking:** Perform mouse clicks using a pinch gesture (thumb + index finger).
- **Dynamic Click Sensitivity** based on hand size.

## 🛠️ Tech Stack
- **Python**
- **OpenCV** - For image processing.
- **MediaPipe** - For hand tracking.
- **PyAutoGUI** - For controlling mouse actions.

## ⚙️ How It Works
1. The webcam captures your hand movements.
2. MediaPipe detects hand landmarks.
3. The index finger’s position controls the mouse cursor.
4. A pinch gesture (thumb + index finger close together) triggers a mouse click.

## 📥 Installation and run
1. **Clone the repository** *(or download the ZIP)*:
```bash
git clone [repository-url]
cd Hand-Controlled Virtual Mouse

pip install opencv-python mediapipe pyautogui
python virtual_mouse.py
