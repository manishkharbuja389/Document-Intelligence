FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for PyMuPDF, faiss, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Run the script that processes documents and starts the API
CMD ["./start.sh"]
