# 1. Set the official Python image as the base
FROM python:3.9-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy all files from the current directory to the /app directory in the container
COPY . /app

# 4. Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Specify the port to be used in the container
EXPOSE 8501

# 6. Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]


