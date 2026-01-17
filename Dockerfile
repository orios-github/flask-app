FROM python:3.9-slim  
# Use the official lightweight Python 3.9 image as the base (Debian slim variant)

WORKDIR /app  
# Set the working directory inside the container to /app

COPY requirements.txt .  
# Copy requirements.txt from your local machine into the container’s /app directory

RUN pip install -r requirements.txt  
# Install all Python dependencies listed in requirements.txt

COPY app.py .  
# Copy your application code (app.py) into the container’s /app directory

CMD ["python", "app.py"]  
# Define the default command: run app.py using Python when the container starts
