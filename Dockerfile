FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential wget git && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Copy only code, not models
COPY . /app

# (Optional) Build llama.cpp if needed
# RUN git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp && make

# Install Python dependencies (add to requirements.txt as needed)
# RUN pip install -r requirements.txt

# Entrypoint (change as needed)
CMD ["python", "ensemble/test_harness.py"]

# Note: Mount models/ as a volume when running the container
# Example: docker run -v $(pwd)/models:/app/models eidolon:latest 