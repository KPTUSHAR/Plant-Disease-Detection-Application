# 📦 Library Imports
import numpy as np
import streamlit as st
import cv2
from PIL import Image
from tensorflow.keras.models import load_model   # ✅ use tensorflow.keras
import tensorflow as tf
import base64
import requests
from streamlit_lottie import st_lottie

# 🚀 Load the Model
model = load_model('plant_disease_model.h5')   # ensure file exists

# 🌱 Class Labels
CLASS_NAMES = ('Tomato-Bacterial_spot', 'Potato-Early_blight', 'Corn-Common_rust')

# 🖼️ Set Page Config
st.set_page_config(page_title="Plant Disease Detector", layout="wide")

# 🔗 Function to Encode Image as Base64
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 🎨 Custom CSS Styling with Embedded Background
img_base64 = get_base64_of_image("img1.jpg")  # Ensure img1.jpg is in same folder

# 🔗 Encode Logo Image (img2.png) as Base64
logo_base64 = get_base64_of_image("img2.png")  # Ensure img2.png is in the same folder


st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container {{
            background: rgba(255, 255, 255, 0.15);
            padding: 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            max-width: 850px;
            width: 100%;
            box-sizing: border-box;
            margin: 2rem;
            margin-top: 6rem;
            margin-bottom: 4rem;
        }}
        h1 {{
            color: #2e8b57;
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            text-shadow: 2px 2px 4px #a9a9a9;
        }}
        .hover-title {{
            color: #2e8b57;
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            text-shadow: 2px 2px 4px #a9a9a9;
            transition: color 0.3s ease, transform 0.3s ease;
        }}
        .hover-title:hover {{
            color: #76c893;
            transform: scale(1.05);
            text-shadow: 3px 3px 6px #555;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# 🔄 Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ Valid Lottie URLs
lottie_upload = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_j1adxtyb.json")
lottie_detect = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_result = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")

# 🧭 Sidebar Navigation
st.sidebar.header("🌿 Navigation")
st.sidebar.markdown("Use this app to detect plant diseases from leaf images quickly and accurately.")
st.sidebar.info("📷 Upload a clear, well-lit leaf image to begin analysis.")

st.sidebar.subheader("📝 How to Use")
st.sidebar.markdown("""
1. **Upload Leaf Image**  
   - Select a single leaf photo with good lighting and no blur.  
   - Make sure the leaf fills most of the frame.

2. **Run Detection**  
   - Click the detection button after uploading.  
   - The model will analyze the image and classify the disease.

3. **View Results**  
   - See the predicted disease name.  
   - Recommended treatment steps will also be displayed.  
""")

# 🔗 Logo at Top-Left of Glass Container
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .block-container {{
            background: rgba(255, 255, 255, 0.15);
            padding: 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            max-width: 850px;
            width: 100%;
            box-sizing: border-box;
            margin: 2rem;
            margin-top: 5rem;
            margin-bottom: 3rem;
            position: relative;
        }}
        .logo-top-left {{
            position: absolute;
            top: 0px;
            left: 0px;
            width: 100px;
            z-index:-10;
        }}
        .centered-title {{
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            color: #2e8b57;
            text-shadow: 2px 2px 4px #a9a9a9;
            margin-top: 0.5rem;
            transition: color 0.3s ease, transform 0.3s ease;
        }}
        .centered-title:hover {{
            color: #76c893;
            transform: scale(1.05);
            text-shadow: 3px 3px 6px #555;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# 🏷️ App Title Inside Glass Container
st.markdown(
    f"""
    
        <img src="data:image/png;base64,{logo_base64}" class="logo-top-left" alt="logo">
        <h1 class="centered-title">PhytoScan</h1>
    
    """,
    unsafe_allow_html=True
)



# 🧩 Tabs as Navigation Steps
tab1, tab2, tab3 = st.tabs(["📤 Step 1: Upload", "🔍 Step 2: Detect", "📊 Step 3: Results"])

with tab1:
    st.subheader("Upload a clear image of the leaf")
    st_lottie(lottie_upload, height=200)
    plant_image = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])
    st.markdown("Make sure the image is well-lit and focused.")

with tab2:
    st.subheader("Run the Disease Detection Model")
    st_lottie(lottie_detect, height=200)
    submit = st.button("🔍 Predict Disease")

with tab3:
    st.subheader("View Prediction and Management Tips")
    st_lottie(lottie_result, height=200)

    if submit:
        if plant_image is not None:
            file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
            opencv_image = cv2.imdecode(file_bytes, 1)
            opencv_image_rgb = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(opencv_image_rgb)
            st.image(pil_image, caption="Uploaded Leaf Image", width=300)

            opencv_image = cv2.resize(opencv_image, (256, 256))
            opencv_image = opencv_image.reshape(1, 256, 256, 3)

            Y_pred = model.predict(opencv_image)
            result = CLASS_NAMES[np.argmax(Y_pred)]
            plant, disease = result.split('-')

            with st.container():
                st.success(f"✅ This is a **{plant}** leaf with **{disease}**.")

            with st.container():
                st.markdown("""
                ### 🌿 Management Tips:
                - 🗑️ Remove infected leaves immediately (prevents spore cycling).
                - 💧 Spray **Chlorothalonil, Mancozeb, or Copper oxychloride** — these work, home remedies don’t.
                - 🌬️ Improve airflow around plants; dense planting = repeat infection.
                - 🚫 Avoid watering on leaves; overhead irrigation accelerates disease.
                - 📅 Follow a strict **7–10 day fungicide schedule** until spread stops.
                """)
        else:
            st.warning("⚠️ Please upload an image before clicking Predict.")