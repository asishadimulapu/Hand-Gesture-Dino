# ✋ Hand Gesture Controlled Jumping (Space Key Simulation)

This project allows you to **control the space bar (jump)** in any game (like Chrome Dino) using your **hand gestures detected via webcam**. When you close your fist, it triggers the **space key press**, enabling touchless interaction.

---

## 🎯 **Features**

✅ Uses **OpenCV** for video capture and frame processing  
✅ Utilises **cvzone HandTrackingModule** for robust hand detection  
✅ Detects finger positions and counts using **mediapipe-based tracking**  
✅ Triggers **space key press** when the fist is closed (all fingers down)  
✅ Real-time frame overlay with gesture status (Jumping / Not Jumping)  
✅ UI overlay for enhanced user feedback  
✅ Works seamlessly with **Windows games and applications**

---

## 🚀 **Setup Instructions**

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hand-gesture-space-control.git
   cd hand-gesture-space-control
Install dependencies:

bash
Copy
Edit
pip install opencv-python cvzone mediapipe
Ensure you have the following files in the same directory:

main.py (code above)

keys.py (contains PressKey, ReleaseKey, and space_pressed)

Run the program:

bash
Copy
Edit
python main.py
🖥️ How It Works
Uses your webcam feed to detect your hand.

Checks finger states:

If all fingers are down (closed fist) ➔ Presses Space key.

Otherwise ➔ Releases Space key.

🎥 Demo
(Attach a short GIF or video here demonstrating your hand controlling jump in Dino game)

📂 File Structure
arduino
Copy
Edit
main.py          # Runs webcam, detects gesture, controls key press
keys.py          # Contains ctypes definitions to press/release keys
README.md
🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss your proposed change.

📜 License
This project is licensed under the MIT License.

🙋 Author
Your Name
LinkedIn
GitHub

⭐ If you like this project, don't forget to star it!
markdown
Copy
Edit

---

### 🔗 **LinkedIn Post Features**

Here is a **LinkedIn post draft** to showcase your project professionally:

---

🚀 **Just completed an exciting project!**

I developed a **Hand Gesture Controlled Jumping System** using **Python, OpenCV, and cvzone**. 🖐️💻

🔑 **Key Features:**
- Controls the **space key using hand gestures** via webcam.
- Detects **fist closure to trigger jump** in games like Chrome Dino.
- Real-time **finger detection and status UI overlay**.
- Uses **mediapipe-based tracking** for accurate gesture recognition.
- Integrates with any Windows application or game requiring space bar input.

💡 **Tech Stack:**
Python, OpenCV, cvzone, mediapipe, ctypes (for virtual key press).

🎯 **Use Cases:**
- Gesture-based gaming
- Touchless human-computer interaction prototypes
- Accessibility tools for users with limited keyboard usage

🔗 **Check out my GitHub repository:**
[github.com/](#)

✨ **Next Goals:**
- Extend to support swipe gestures for left/right key presses
- Integrate with full body tracking for immersive gaming experiences

🙌 **Feedback and suggestions are welcome!**

#OpenCV #Python #ComputerVision #GestureRecognition #cvzone #Projects #AI #ML #Innovation #Accessibility #Gaming
