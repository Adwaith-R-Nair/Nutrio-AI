import streamlit as st
import base64

# --- Page config ---
st.set_page_config(
    page_title="NUTRIO",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Background video ---
video_url = "https://www.pexels.com/download/video/3196094/"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

/* --- General --- */
html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow: hidden;
    font-family: 'Quicksand', sans-serif;
}}
.stApp {{
    background: transparent;
}}

/* --- Background Video --- */
video.bg {{
    position: fixed;
    right: 0;
    top: 50%;
    left: 50%;
    bottom: 0;
    min-width: 100%;
    min-height: 100%;
    z-index: -1;
    object-fit: contain;
    transform: translate(-50%, -50%);
    opacity: 1;
}}

/* --- Hero Section --- */
.hero {{
    position: absolute;
    top: 12vh;
    left: 6vw;
    z-index: 2;
}}

.hero .title {{
    font-size: 120px;
    font-weight: 700;
    color: #00FFD1;
    text-shadow: 0 0 6px #00FFD1, 0 0 12px rgba(0, 255, 209, 0.2);
    letter-spacing: -2px;
    animation: glow 2.5s ease-in-out infinite alternate;
}}

.hero .tagline {{
    font-size: 32px;
    font-weight: 500;
    color: #FFFFFFCC;
    margin-top: 10px;
    text-shadow: 0 0 10px rgba(255,255,255,0.5);
    animation: fadeIn 2s ease-in-out;
}}

/* --- Upload Card Glassmorphism --- */
div[data-testid="stFileUploader"] {{
    margin-top: 600px;
    background: rgba(255, 255, 255, 0.15) !important;
    backdrop-filter: blur(10px);
    border-radius: 20px !important;
    padding: 1.2rem !important;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    border: 1px solid rgba(255, 255, 255, 0.3);
}}

/* --- Button Styling --- */
.stButton>button {{
    background: linear-gradient(90deg, #00FFD1, #00A6FF);
    color: white !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 0.8rem 1.5rem;
    border-radius: 14px !important;
    border: none;
    box-shadow: 0 4px 18px rgba(0,0,0,0.3);
    transition: all 0.3s ease-in-out;
}}
.stButton>button:hover {{
    transform: scale(1.05);
    box-shadow: 0 6px 25px rgba(0,0,0,0.5);
}}

/* --- Uploaded Image --- */
.stImage img {{
    border-radius: 16px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
    margin-top: 20px;
}}

/* --- Animations --- */
@keyframes glow {{
    0% {{ text-shadow: 0 0 6px #00FFD1, 0 0 12px rgba(0, 255, 209, 0.2); }}
    50% {{ text-shadow: 0 0 10px #00FFD1, 0 0 20px rgba(0, 255, 209, 0.25); }}
    100% {{ text-shadow: 0 0 6px #00FFD1, 0 0 12px rgba(0, 255, 209, 0.2); }}
}}

@keyframes fadeIn {{
    0% {{ opacity: 0; transform: translateY(20px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}
</style>

<video autoplay muted loop class="bg">
    <source src="{video_url}" type="video/mp4">
</video>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="hero">
    <div class="title">NUTRIO</div>
    <div class="tagline">Know your plate, every time.</div>
</div>
""", unsafe_allow_html=True)

# --- Layout: uploader on right ---
col1, col2 = st.columns([2, 1])

with col2:
    uploaded_file = st.file_uploader(
        "Upload your meal image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

# --- After upload ---
if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    col1, col2 = st.columns([3, 1])

    with col2:
        st.image(file_bytes, width=220, caption="Your Uploaded Plate 🍽")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Describe Plate"):
            st.switch_page("pages/plate.py")
