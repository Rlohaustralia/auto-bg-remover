import streamlit as st
from rembg import remove
from PIL import Image
import io
import zipfile
from io import BytesIO
import base64
from utils import create_image_with_download_button


def main():
    # Page Config
    st.set_page_config(layout="wide", page_title="Background Remover")
    st.write("__Background Removal Web App__")
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    # License
    license_text = """
    MIT License

    Copyright (c) 2021 Johnathan Nader
    Copyright (c) 2020 Lucas Nestler
    Copyright (c) 2020 Dr. Tim Scarfe
    Copyright (c) 2020 Daniel Gatis

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """
    st.write(license_text)
    st.markdown("<br>" * 2, unsafe_allow_html=True)

    # Allowed file types (multiple files)
    uploaded_files = st.file_uploader("Choose an image... 𓂀", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if uploaded_files is not None:
        processed_images = []

        for uploaded_file in uploaded_files:
            # Split the layout into two columns
            col1, col2 = st.columns(2)

            try:
                # Load the image
                image = Image.open(uploaded_file)

                # Get image details
                img_size = image.size
               
                # Format caption
                caption = f"{uploaded_file.name} {img_size}"

                with col1:
                    st.image(image, caption=caption, use_column_width=True)

                with col2:
                    with st.spinner('Removing background...'):
                        # Convert the image to binary file
                        buffer = io.BytesIO()
                        image.save(buffer, format="PNG")
                        input_data = buffer.getvalue()

                        # Call the background remover function
                        output_data = remove(input_data)
                        output_image = Image.open(io.BytesIO(output_data))

                        # Generate HTML for image and download button
                        img_name = uploaded_file.name.rsplit('.', 1)[0] + '.png'
                        html_code = create_image_with_download_button(output_image, img_name)

                        # Render HTML in Streamlit
                        st.markdown(html_code, unsafe_allow_html=True)

                # Save processed images
                processed_images.append((output_image, uploaded_file.name))

            except Exception as e:
                st.error(f"Error: {e}")

        if processed_images:
            st.success('All Done!')

            # Create a zip file in memory
            zip_buffer = BytesIO()

            # Create a new zip file inside the 'zip_buffer'
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
                for img, img_name in processed_images:
                    # Strip original extension and add PNG
                    final_img_name = img_name.rsplit('.', 1)[0]

                    # This buffer will hold the binary data of the processed image
                    img_buffer = BytesIO()
                    img.save(img_buffer, format='PNG')

                    # Write the processed image in PNG format into the zip file
                    zip_file.writestr(f"processed_{final_img_name}.png", img_buffer.getvalue())

            zip_buffer.seek(0)
            st.download_button(
                label="Download Images as Zip",
                data=zip_buffer,
                file_name="processed_images.zip",
                mime="application/zip"
            )

    footer = """
        ---
            © 2024 8DIVISION. All rights reserved.
            New Standard, Inc  8DIVISION, 31 Toegye-ro 118-gil, Jung-gu, Seoul, Republic of Korea  +82 70-4135-0038   Business Registration Number: 692-81-02223
            Representative: In-Chan Oh, Shin-Gu Heo, Sang-Ho Park  Mail order business report number: 2021-Seoul Jung-gu 2467  info@8division.com
        """
    st.markdown(footer)

if __name__ == "__main__":
    main()
