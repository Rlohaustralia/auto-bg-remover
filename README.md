## Background Removal Web App

This is a **Background Removal Web App** built with Streamlit and the `rembg` library. It allows users to upload images, remove their backgrounds, and download the processed images. The application supports multiple image formats and provides a simple and intuitive user interface for seamless background removal.
</br>
</br>
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
   🚩 **Eliminating version and dependency issues by using Docker**</br>
- **Problem:** When deploying the app from the local environment to EC2, issues occurred due to differences in library dependencies and server configurations. Code that worked locally ran into errors on EC2, requiring manual adjustments. The main issues were Python version and package version mismatches between the two environments.</br>
- **Solution:** To fix this, Docker was introduced. The packages from requirements.txt were installed within the Docker image, ensuring the app ran the same on both local and EC2. </br>
- **What I learned:** I learned that Docker simplifies deployment by ensuring consistent environments, eliminating version and dependency issues, and improving app stability across platforms.</br></br>

  
2️⃣ **While I knew that DNS acts as a directory for IP addresses, I didn't fully understand the connection process** </br>
   🚩 **Learning the roles of Registrant, Registrar, and Registry, along with how name servers forward requests, clarified the process**</br>
- **Problem:** After purchasing a domain from GoDaddy, I was unsure how to connect it to the Elastic IP of my EC2 instance. While I knew that DNS acts like a directory for IP addresses, I didn't fully understand the steps required to achieve this connection. Though I was able to connect the domain to the EC2 instance through online searches, the process felt somewhat magical, and I wanted to gain a deeper understanding of how DNS works.</br>
- **Solution:** Through further research, I learned that multiple entities are involved in this process: the Registrant (Client), the Registrar (e.g., GoDaddy), and the Registry (Top-level domain operators). Each operates its own name servers, which forward requests to the appropriate IP addresses to complete the connection. I studied how these entities interact to route traffic to my EC2 instance via DNS. </br>
- **What I learned:** I gained a clearer understanding of how DNS operates and how multiple entities such as the Registrar, Registry, and name servers are involved in directing user requests to the correct IP address (in this case, my EC2 instance). The process is more complex than it initially appears, with each entity playing a critical role in handling domain connections.</br></br>


3️⃣ **Changing HTTP to HTTPS** </br>
   🚩 **Redirecting using SSL Certificate & Load Balancer**</br>
- **Problem:** Successfully connected the domain to the EC2 instance, but HTTPS access was not working, while HTTP worked. Although I knew SSL certificates were needed for secure connections, I was unsure where to obtain one. After researching, I found that Let’s Encrypt offers free SSL certificates, but installing them on GoDaddy hosting is difficult due to automated certificate issuance and renewal issues. GoDaddy's own automated renewal comes at an extra cost, so I looked for alternatives and discovered that I could obtain a free SSL certificate through AWS Certificate Manager (ACM) and use it with the Elastic Load Balancer (ELB). Despite completing the SSL certificate configuration, load balancer setup, target group settings, security group settings, and DNS record configurations, I still could not connect via HTTPS. I spent considerable time troubleshooting due to my unclear understanding of how Route 53 and the Load Balancer worked.</br>
- **Solution:** After understanding the architecture involving Route 53, ACM, and the Load Balancer, I grasped the port mapping process. The Load Balancer was initially set to route HTTPS traffic to port 80 on the EC2 instance, mapping port 443 to port 80, with traffic from port 80 directed to port 8501 (Streamlit port) in the Docker container. The failure to do this successfully was due to the absence of an Nginx reverse proxy configuration to forward requests from port 80 to Streamlit’s port 8501. The app could operate without Nginx due to its simple structure, and since the Load Balancer could handle SSL processing, I modified the settings to map incoming traffic on port 443 directly to port 8501, which worked successfully. </br>
- **What I learned:** I gained a deaper understanding of the architecture involving AWS Certificate Manager, Elastic Load Balancer, and Route 53, particularly the crucial role of port mapping in ensuring that traffic flows correctly between different ports and services. This knowledge allowed me to configure my application for secure HTTPS connections effectively. </br></br>


4️⃣ **The app loaded successfully but encountered 504 error when uploading images for background removal** </br>
   🚩 **Managing CPU and memory usage to enhance performance**
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


5️⃣ **Automatic Docker Shutdown on Timeout Errors** </br>
   🚩 **Using configuration files to minimize downtime and ensure availability**
- **Problem:** When a 504 Gateway Timeout error occurred, it led to subsequent 502 Bad Gateway errors.</br>
- **Solution:** Initially, I had to manually restart Docker whenever a 502 error occurred, which was highly inefficient. To address this, I explored environment file configurations and modified the docker-compose.yml file to include restart: unless-stopped. This change ensured that the application restarts automatically if it encounters errors. As a result, the 502 error pages were eliminated, and refreshing the page now works seamlessly. </br>
- **What I learned:** I learned the importance of configuring files because if a container stops due to an error or failure, it will automatically restart, minimizing downtime and ensuring the application remains available.</br></br>


6️⃣ **The app was accessible via HTTP, but HTTPS caused issues**</br>
   🚩 **Using Nginx and AWS Certificate Manager (ACM) to enable HTTPS**
- **Problem:** After deploying a Dockerized Streamlit app to EC2, it was accessible via HTTP by mapping port 80 to Streamlit’s internal port 8501. However, attempting to access the app over HTTPS led to browser security warnings. Streamlit does not support HTTPS natively, and no SSL certificate was configured at that point.</br>
- **Solution:** To enable HTTPS, I added Nginx as a reverse proxy in front of the Streamlit app. Nginx was configured to listen on port 443 and forward incoming HTTPS requests to the internal Streamlit service running on port 8501. For SSL, I used AWS Certificate Manager (ACM) to issue a free SSL certificate and integrated it with an AWS Application Load Balancer (ALB). The load balancer handled HTTPS termination, and forwarded traffic securely to the EC2 instance running Nginx and Docker.</br>
- **What I learned:** I learned how HTTPS can be enabled through different layers—either directly via Nginx with a Certbot-issued certificate, or using AWS-managed certificates via ACM and an ALB. This experience deepened my understanding of cloud infrastructure, load balancing, and secure production deployment best practices.
</br></br>




## Future Improvements
✔️ Ordered by priority</br>
- **Improve image processing time:** Improve the app's ability to handle large data more efficiently, possibly through image resizing strategy, converting images to more efficient formats like webp, or Batch Processing Techniques.
- **Enhanced error handling:** Provide more specific and user-friendly error messages when image processing fails, including possible solutions or retry options.
- **Background removal improvement:** Enhance the background removal algorithm for better accuracy with white and light-colored clothing or jewelry by applying multiple models or introducing a different model to adjust the background to a darker shade, thereby increasing contrast and minimizing post-processing needs.
- **Mobile optimization:** Ensure the UI is fully responsive and optimized for mobile devices.
- **Image format options for download:** Allow users to choose different image formats (e.g., JPG, TIFF) for download rather than just PNG.
- **Language support:** Add multi-language support for non-English users.
</br>
</br>
