## Background Removal Web App

This is a **Background Removal Web App** built with Streamlit and the `rembg` library. It allows users to upload images, remove their backgrounds, and download the processed images. The application supports multiple image formats and provides a simple and intuitive user interface for seamless background removal.

## Live web app
[https://autobgremover.streamlit.app/](https://autobgremover.com/)
<img width="1426" alt="Screenshot" src="https://github.com/user-attachments/assets/12535b4a-90e8-4d25-8afe-c7673b5ba146">


## Features

- Upload multiple image files (JPG, PNG, JPEG, WEBP).
- Remove the background from uploaded images using the `rembg` library.
- Preview the original and processed images.
- Download processed images individually or as a ZIP file.
- Fully integrated with Streamlit for an easy-to-use web interface.

## Installation

To run this application locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   
2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   On Windows:
   venv\Scripts\activate
   On macOS/Linux:
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the Streamlit application:
   streamlit run app.py

## Usage
Open the application: Navigate to http://localhost:8501 in your web browser.
Upload images: Click on the file uploader to select multiple image files.
Process images: The app will display the uploaded images and process them to remove their backgrounds.
Download results: Download processed images individually or as a ZIP file.
