FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install OS & build dependencies (especially for pyaudio)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    curl \
    gcc \
    libasound2-dev \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose Gradio port
EXPOSE 7860

# Start the Gradio app
CMD ["python", "gradio_app.py"]
