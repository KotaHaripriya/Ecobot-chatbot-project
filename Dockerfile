FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl unzip wget gnupg ca-certificates fonts-liberation libnss3 libxss1 \
    libappindicator3-1 libasound2 libatk-bridge2.0-0 libgtk-3-0 \
    libgbm1 libx11-xcb1 xvfb chromium chromium-driver \
    && apt-get clean

# Set display for headless Chrome
ENV DISPLAY=:99

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8501

# Run the app with Xvfb (virtual display)
CMD xvfb-run streamlit run app.py --server.port=8501 --server.address=0.0.0.0
