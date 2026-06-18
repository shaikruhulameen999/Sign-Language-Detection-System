🤟 Sign Language Detection System

🚀 A real-time Sign Language Detection Web Application built using Python, Streamlit, MediaPipe, and OpenCV.
This project uses computer vision to recognize hand gestures from a live webcam feed and display the detected sign in real time.

📌 Demo

🎥 Real-time webcam-based sign detection inside browser using Streamlit WebRTC.

🧠 Tech Stack
🐍 Python
🎈 Streamlit
📡 streamlit-webrtc
🤟 MediaPipe (Hand Tracking)
👁️ OpenCV
🧮 NumPy
⚙️ Features

✔ Real-time hand tracking using webcam
✔ Browser-based live video streaming
✔ Detects multiple hand gestures
✔ Clean Streamlit UI
✔ Modular backend structure
✔ Fast and lightweight processing

✋ Supported Gestures
✊ FIST
✋ FIVE
☝ ONE
✌ VICTORY
👍 THUMBS UP
🤟 LOVE YOU
🏗️ Project Structure
Sign-Language-Detection-System/
│
├── app.py
├── backend/
│   ├── hand_landmarker.py
│   ├── gesture_rules.py
│   ├── camera_stream.py
│   └── drawing_utils.py
│
├── models/
│   └── hand_landmarker.task
│
├── requirements.txt
└── README.md
🚀 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/Sign-Language-Detection-System.git
cd Sign-Language-Detection-System
2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the app
streamlit run app.py
📦 Requirements.txt
streamlit
streamlit-webrtc
opencv-python
mediapipe
numpy
av
💡 How It Works
Captures live webcam feed using WebRTC
Processes frames using OpenCV
Detects hand landmarks using MediaPipe
Applies gesture rules to classify signs
Displays result in Streamlit UI
🎯 Future Improvements
Add full alphabet sign language detection (A-Z)
Improve accuracy with ML/DL model
Add voice output (Text-to-Speech)
Mobile support
Multi-hand detection
👨‍💻 Author

Shaik Ruhul Ameen
💼 Aspiring AI/ML Developer
📌 Passionate about Computer Vision & Real-Time AI Apps
