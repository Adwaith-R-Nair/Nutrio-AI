import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Your Plate", layout="wide", page_icon="🥗")

# --- Background image ---
bg_url = "https://images.pexels.com/photos/4226794/pexels-photo-4226794.jpeg?cs=srgb&dl=pexels-karola-g-4226794.jpg&fm=jpg&_gl=1*1e0dn7j*_ga*MTcwNzg1MzQyMy4xNzYwOTg5NjEx*_ga_8JE65Q40S6*czE3NjEwNjc5OTgkbzMkZzEkdDE3NjEwNjgwNDYkajEyJGwwJGgw"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');

/* --- General --- */
html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    overflow-x: hidden;
    font-family: 'Quicksand', sans-serif;
}}

.stApp {{
    background: url('{bg_url}') no-repeat center center fixed;
    background-size: cover;
}}

/* --- Overlay to darken background --- */
.overlay {{
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.35);
    z-index: 0;
}}

/* --- Floating decorative circles --- */
.circle {{
    position: fixed;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: rgba(210, 180, 140, 0.2); /* soft neon brown */
    filter: blur(50px);
    z-index: 1;
}}

.circle.left {{
    top: 20%;
    left: 50px;
}}

.circle.right {{
    bottom: 15%;
    right: 60px;
}}

/* --- Hero Title --- */
.hero {{
    position: relative;
    text-align: center;
    margin-top: 8vh;
    z-index: 2;
}}

.hero h1 {{
    font-size: 72px;
    font-weight: 700;
    color: #D2B48C;  /* light neon brown */
    text-shadow: 0 0 6px #D2B48C, 0 0 12px rgba(210, 180, 140, 0.2);
    animation: fadeIn 2s ease-in-out;
}}

/* --- Glassmorphic Card --- */
.card {{
    position: relative;
    max-width: 700px;
    margin: 60px auto 0 auto;
    padding: 2rem;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    color: #fff;
    z-index: 2;
    animation: fadeIn 2.5s ease-in-out;
}}

.card h2 {{
    color: #D2B48C;  /* light neon brown */
    font-weight: 700;
    font-size: 36px;
    margin-bottom: 15px;
    text-shadow: 0 0 4px #D2B48C, 0 0 8px rgba(210, 180, 140, 0.2); /* subtle glow */
}}

.card p {{
    font-size: 20px;
    color: #e0e0e0;
    line-height: 1.5;
}}

.card button {{
    background: linear-gradient(90deg, #D2B48C, #E6C38C); /* soft brown gradient */
    color: white;
    font-weight: 600;
    font-size: 16px;
    padding: 0.7rem 1.5rem;
    border-radius: 14px;
    border: none;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
    cursor: pointer;
    transition: all 0.3s ease-in-out;
}}
.card button:hover {{
    transform: scale(1.05);
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
}}

/* --- Animations --- */
@keyframes fadeIn {{
    0% {{ opacity: 0; transform: translateY(20px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}
</style>

<div class="overlay"></div>
<div class="circle left"></div>
<div class="circle right"></div>

<div class="hero">
    <h1>Your Plate</h1>
</div>
""", unsafe_allow_html=True)

# --- Glassmorphic Card Content ---
st.markdown("""
<div class="card">
    <h2>Plate Analysis</h2>
    <p>Here your AI results will be displayed. For example: food items, portion size, calories, and nutritional info. Once you upload your meal image, this card will dynamically update with all the relevant details in a visually stunning format.</p>
    <button>Analyze Again</button>
</div>
""", unsafe_allow_html=True)
