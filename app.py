import streamlit as st
from rembg import remove
from PIL import Image
import io

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

    # Allowed file types
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        try:
            # 업로드된 파일을 PIL 이미지 객체로 변환
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Show image info
            print(image.format)  # JPEG, PNG, 등
            print(image.size)    # (width, height)
            print(image.mode)    # RGB, L, 등


            with st.spinner('Removing background...'):
                # Convert the image to binary file
                buffer = io.BytesIO()
                image.save(buffer, format="PNG")
                input_data = buffer.getvalue()

                # Call the backgound remover function
                output_data = remove(input_data)
                output_image = Image.open(io.BytesIO(output_data))

            st.image(output_image, caption='Processed Image', use_column_width=True)
            st.success('Background removed successfully!')

            # Text input for custom file name
            default_filename = "processed_img.png"
            file_name = st.text_input("Enter file name: ", value=default_filename)

            # Download image
            st.download_button(
                label="Download Image",
                data = output_data,
                file_name = "f{file_name}.png",
                mime = "image/png"
            )
        except Exception as e:
            st.error(f"Error: {e}")
  
    
    footer = """
        ---
            © 2024 8DIVISION. All rights reserved.
            New Standard, Inc  8DIVISION, 31 Toegye-ro 118-gil, Jung-gu, Seoul, Republic of Korea  +82 70-4135-0038   Business Registration Number: 692-81-02223
            Representative: In-Chan Oh, Shin-Gu Heo, Sang-Ho Park  Mail order business report number: 2021-Seoul Jung-gu 2467  info@8division.com
            
        """
    st.markdown(footer)

if __name__ == "__main__":
    main()
