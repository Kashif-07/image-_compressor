import streamlit as st
from PIL import Image

st.title("Image Compressor")
#st.header
st.write("Reduce the file size of your images with online image compressor.Compresse Image  files quickly without software installation.")

# Create a file input widget and get the selected file
file = st.file_uploader("Select an image file", type=["jpg", "jpeg", "png"])

if file is not None:
    # Open the image using PIL
    img = Image.open(file)

    # Display the image
    st.image(img, caption="Selected Image", use_column_width=True)

    # Get the dimensions of the image
    width, height = img.size

    # Create a slider to allow the user to select the compression level
    compression_level = st.slider("Compression Level", min_value=1, max_value=10, value=5)

    # Compress the image using PIL
    compressed_img = img.resize((int(width/compression_level), int(height/compression_level)), Image.ANTIALIAS)

    # Convert the image to RGB mode
    if compressed_img.mode == 'RGBA':
        compressed_img = compressed_img.convert('RGB')

    # Create a file output widget and get the path to save the compressed image
    save_path = st.text_input("Save As", value="compressed.jpg")
    if save_path:
        compressed_img.save(save_path)

        # Display a success message
        st.success("Image compressed and saved successfully!")
