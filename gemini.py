import streamlit as st
import google.generativeai as genai
import tempfile
import os
from PIL import Image  # ✅ Import PIL for image processing

# 🔑 Set Your Gemini API Key
GEMINI_API_KEY = "AIzaSyALT2tH4gMtyqRc2oN7wdoOV5VSE0yfrS8"

# Initialize Gemini AI with API Key
genai.configure(api_key=GEMINI_API_KEY)

def generate_image_description(image_path):
    """
    Function to generate an image description using Gemini Pro Vision.
    Parameters:
    - image_path: The file path of the image to be analyzed.
    Returns:
    - A text description of the image.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")

    # ✅ Open the image using PIL to ensure correct format
    image = Image.open(image_path)

    # ✅ Send the properly formatted image to Gemini Pro Vision
    response = model.generate_content([image, "Describe this image."])
    
    # Extract and return the generated description
    return response.text if response else "No description generated."

def main():
    """
    Main function to run the Streamlit web application.
    """
    st.title("Gemini AI Image Description")
    
    # Allow users to upload an image
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_image:
        # Save the image temporarily
        temp_dir = tempfile.mkdtemp()
        image_path = os.path.join(temp_dir, uploaded_image.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_image.getvalue())

        # ✅ Display the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # ✅ Generate and display the image description
        if st.button("Generate Description"):
            description = generate_image_description(image_path)
            st.header("Image Description")
            st.write(description)

# Run the app
if __name__ == "__main__":
    main()


