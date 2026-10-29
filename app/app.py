import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

# Model Path
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "best_model.h5"
)

# Load Model
model = tf.keras.models.load_model(MODEL_PATH)

classes = [
    "glioma",
    "meningioma",
    "no_tumor",
    "pituitary"
]

st.set_page_config(
    page_title="Brain Tumor Classification",
    page_icon="🧠"
)

st.title("🧠 Brain Tumor Classification")
st.write("Upload an MRI image for prediction")

uploaded_file = st.file_uploader(
    "Choose an MRI image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded MRI Image",
        use_container_width=True
    )

    image = image.resize((224, 224))

    image = np.array(image)

    image = np.expand_dims(image, axis=0)

    image = preprocess_input(image)

    prediction = model.predict(image)

    predicted_class = classes[np.argmax(prediction)]

    confidence = np.max(prediction) * 100

    st.success(
        f"Prediction: {predicted_class}"
    )

    st.info(
        f"Confidence: {confidence:.2f}%"
    )