from io import BytesIO
import base64

def create_image_with_download_button(image, file_name):
    """ Create HTML and JavaScript for an image with a download button that appears on hover """
    # Convert image to bytes
    img_buffer = BytesIO()
    image.save(img_buffer, format="PNG")
    img_data = img_buffer.getvalue()
    img_data_uri = "data:image/png;base64," + base64.b64encode(img_data).decode("utf-8")

    # Create HTML with embedded JavaScript
    html_code = f"""
    <style>
        .image-container {{
            position: relative;
            display: inline-block;
            margin: 10px;
        }}
        .download-btn {{
            display: none;
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #ffffff;
            color: white;
            border: none;
            padding: 5px 10px;
            cursor: pointer;
            border-radius: 5px;
        }}
        .image-container:hover .download-btn {{
            display: block;
        }}
    </style>
    <div class="image-container">
        <img src="{img_data_uri}" style="width: 100%; height: auto;" />
        <a class="download-btn" href="{img_data_uri}" download="{file_name}">Download</a>
    </div>
    """
    return html_code