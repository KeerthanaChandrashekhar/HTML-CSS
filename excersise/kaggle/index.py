import http
import os
import base64
import google.generativeai as genai
import streamlit as st
from PIL import Image

# Title of the app
st.title("Animal spieses identification")

if st.button("Exit App"):
    st.warning("You have exited the app. Refresh the page to start over.")
    st.stop()  # Stops further execution of the script

# File uploader
uploaded_file = st.file_uploader("Upload an image of Animal", type=["jpg", "jpeg", "png"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.success("Image uploaded successfully!")
else:
    st.info("Please upload an image.")
    
def getImgData(url:str):
    genai.configure(api_key="AIzaSyB5F3mRxEOlbyyq0ZlE_pmGCkqPlVdzJo8")
    model = genai.GenerativeModel(model_name = "gemini-1.5-pro")
    image_path = url

    image = httpx.get(image_path)

    prompt = "name this animal species and also scientific name"
    response = model.generate_content([{'mime_type':f'image/{url.split(".")[-1]}', 'data': base64.b64encode(image.content).decode('utf-8')}, prompt])

    print(response.text)
getImgData(uploaded_file)

