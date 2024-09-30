## Background Removal Web App

This is a **Background Removal Web App** built with Streamlit and the `rembg` library. It allows users to upload images, remove their backgrounds, and download the processed images. The application supports multiple image formats and provides a simple and intuitive user interface for seamless background removal.
</br>
</br>


## Live web app </br>https://autobgremover.com
<img width="700" alt="Screenshot" src="https://github.com/user-attachments/assets/12535b4a-90e8-4d25-8afe-c7673b5ba146">
<img width="700" alt="Screenshot2" src="https://github.com/user-attachments/assets/9330e12b-ce36-4dd9-9fbd-ce21f15e384a">
</br>
</br>


## Features

- **Multi-image Upload:** Users can upload multiple image files (JPG, PNG, JPEG, WEBP) at once for background removal.
- **Background Removal:** The app uses the rembg library to remove the background from uploaded images.
- **Image Previews:** Users can preview the original and processed images side by side.
- **Image Metadata Display:** Displays the size and name of the uploaded image for user reference.
- **Progress Tracking:** A progress bar displays the background removal progress for multiple images.
- **Download Individual Images:** Provides individual download options for each processed image.
- **Batch Image Download:** Allows users to download all processed images as a ZIP file.
</br>
</br>


## Built with
Python, Streamlit, VS Code, GoDaddy, AWS (ACM, Load Balancer, Route 53, EC2 with Ubuntu)
</br>
</br>


## Architecture
<img width="700" alt="Architecture" src="https://github.com/user-attachments/assets/ac4c667c-e617-4154-992f-0bc1340d85e3">
</br>
</br>


## Issue faced
1️⃣ **The app worked locally but failed after deployment to EC2**</br>
- 🚩**Eliminating version and dependency issues by using Docker**</br>
- **Problem:** When deploying the app from the local environment to EC2, issues occurred due to differences in library dependencies and server configurations. Code that worked locally ran into errors on EC2, requiring manual adjustments. The main issues were Python version and package version mismatches between the two environments.</br>
- **Solution:** To fix this, Docker was introduced. The packages from requirements.txt were installed within the Docker image, ensuring the app ran the same on both local and EC2. </br>
- **What I learned:** I learned that Docker simplifies deployment by ensuring consistent environments, eliminating version and dependency issues, and improving app stability across platforms.</br></br>

  
2️⃣ **The app Worked Locally but Failed After Deployment to EC2** </br>
- **Problem:** When deploying the app from the local environment to EC2, issues occurred due to differences in library dependencies and server configurations. Code that worked locally ran into errors on EC2, requiring manual adjustments. The main issues were Python version and package version mismatches between the two environments.</br>
- **Solution:** To fix this, Docker was introduced. The packages from requirements.txt were installed within the Docker image, ensuring the app ran the same on both local and EC2. </br>
- **What I learned:** I learned that Docker simplifies deployment by ensuring consistent environments, eliminating version and dependency issues, and improving app stability across platforms.</br></br>


3️⃣ **The app loaded successfully but encountered 504 error when uploading images for background removal** </br>
- **Problem:** The web page successfully loaded, but upon uploading images for background removal, the application encountered 504 Gateway Timeout due to communication delays between the server and the client.</br>
- **Solution:**</br>
After rebooting the instance and confirming correct settings for the public IP, DNS, and firewall, I investigated Docker issues. I discovered that the running Docker container had exited automatically due to an "Out of Memory" (OOM) error caused by the Streamlit application consuming excessive memory. To address this:</br>
🧐 I monitored memory usage with the htop command, revealing high CPU usage.</br>
🧐 I initially set up 1GB of swap memory, which reduced CPU load and allowed single image processing. However, further increases were limited by the instance's hardware capacity.</br>
🧐 After deleting unnecessary logs, the CPU load decreased, but performance was still inadequate for processing multiple images.</br>
🧐 Ultimately, I identified that high-resolution image files stored in the Docker container from local testing were degrading performance. After removing these files, the application could successfully handle multiple image processing like in local testing. </br>
- **What I learned:**</br>
✅ Monitoring and managing memory usage is crucial, especially with memory-intensive tasks.</br>
✅ Implementing swap memory can provide temporary relief for memory issues but has limitations based on the instance type.</br>
✅ Regular cleanup of unnecessary files and resources within Docker containers can significantly enhance performance and resource management.</br></br>


4️⃣ **Automatic Docker Shutdown on Timeout Errors** </br>
- **Problem:** When a 504 Gateway Timeout error occurred, it led to subsequent 502 Bad Gateway errors.</br>
- **Solution:** Initially, I had to manually restart Docker whenever a 502 error occurred, which was highly inefficient. To address this, I explored environment file configurations and modified the docker-compose.yml file to include restart: unless-stopped. This change ensured that the application restarts automatically if it encounters errors. As a result, the 502 error pages were eliminated, and refreshing the page now works seamlessly. </br>
- **What I learned:** I learned the importance of configuring files because if a container stops due to an error or failure, it will automatically restart, minimizing downtime and ensuring the application remains available.</br></br>



## Future Improvements
Currently working on (Last updated on September 28, 2024) </br>
✔️ Ordered by priority</br>
- **Improve image processing time:** Improve the app's ability to handle large data more efficiently, possibly through image resizing strategy, converting images to more efficient formats like webp, or Batch Processing Techniques.
- **Enhanced Error Handling:** Provide more specific and user-friendly error messages when image processing fails, including possible solutions or retry options.
- **Background Removal Improvement:** Enhance the background removal algorithm for better accuracy with white and light-colored clothing or jewelry by applying multiple models or introducing a different model to adjust the background to a darker shade, thereby increasing contrast and minimizing post-processing needs.
- **Mobile Optimization:** Ensure the UI is fully responsive and optimized for mobile devices.
- **Image Format Options for Download:** Allow users to choose different image formats (e.g., JPG, TIFF) for download rather than just PNG.
- **Language Support:** Add multi-language support for non-English users.
</br>
</br>
