import sys
import os

# Fix Python path issue (IMPORTANT)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import av
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

# Your backend function
from backend.camara_stream import process_frame


# =========================
# STREAMLIT CONFIG
# =========================
st.set_page_config(
    page_title="Sign Language Detection",
    page_icon="🤟",
    layout="wide"
)

st.title("🤟 Sign Language Detection System")

# =========================
# UI LAYOUT
# =========================
col1, col2 = st.columns([3, 1])

with col2:
    st.info("""
### Supported Signs

✊ FIST  
✋ FIVE  
☝ ONE  
✌ SUCESSFULLY DONE SIGN LANGUAGE RECOGNIZATION  
👍 THUMBS UP  
🤟 LOVE YOU  
🅻 L
""")

# =========================
# VIDEO PROCESSOR
# =========================
class VideoProcessor(VideoProcessorBase):

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Process frame (your ML / MediaPipe logic)
        img = process_frame(img)

        return av.VideoFrame.from_ndarray(
            img,
            format="bgr24"
        )

# =========================
# WEBCAM STREAM
# =========================
with col1:
    webrtc_streamer(
        key="gesture",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )