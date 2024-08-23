import streamlit as st
from rembg import remove
from PIL import Image
import io
import zipfile
from io import BytesIO
import base64
from utils import get_license_text, create_image_with_download_button, get_footer_text


def main():
    # Page Config
    st.set_page_config(layout="wide", page_title="Background Remover")
    
    # Title
    st.write("В⩜𓍹ʞℊ𝐫⚬∪𓎆ძ󠀠󠀠󠀠󠁝󠁝️󠁫󠁜󠁩ㅤƦ꒰ϻ⚬⚺꒰я ㅤㅤㅤㅤㅤ𓃦ㅤㅤㅤㅤㅤ𓍯𓂃 ␥")

    # Insert hidden text as an HTML comment
    st.markdown("<!--Free Background Remover Web App -->", unsafe_allow_html=True)
    st.markdown("<!--무료 누끼 제거 사이트-->", unsafe_allow_html=True)


    # Split the layout into two columns
    col1, col2 = st.columns(2)
    with col1:
        st.image("test_img/bg1.jpg")
    with col2:
        st.image("test_img/bg2.jpg")
    

    # License
    st.markdown("<br>" * 1, unsafe_allow_html=True)

    # Allowed file types (multiple files)
    uploaded_files = st.file_uploader("Choose an image... ⌖", type=["jpg", "png", "jpeg", "webp"], accept_multiple_files=True)


    if uploaded_files is not None:
        processed_images = []

        # Progress bar
        total_files_num = len(uploaded_files)

        if total_files_num > 0:

            progress_bar = st.progress(0)
            progress_step = 1 / total_files_num


            for idx, uploaded_file in enumerate(uploaded_files):

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

                    # Update progress bar for each file
                    progress_bar.progress((idx + 1) * progress_step)

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
    # Footer
    st.markdown(get_footer_text())


if __name__ == "__main__":
    main()
