FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential cmake git wget && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /app

# Clone and build llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    make

# Copy code and config (after building llama.cpp)
COPY . /app

# Set llama_cpp_path in config.yaml to the correct location
RUN sed -i 's|llama_cpp_path:.*|llama_cpp_path: llama.cpp/main|' /app/config.yaml || true

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Entrypoint (change as needed)
CMD ["python", "ensemble/test_harness.py"]

# Note: Mount models/ as a volume when running the container
# Example: docker run -v $(pwd)/models:/app/models eidolon:latest 