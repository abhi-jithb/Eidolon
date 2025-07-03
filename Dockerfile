FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential cmake git wget libcurl4-openssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy code and config first
COPY . /app

# Build llama.cpp with CMake after code is copied
RUN git clone https://github.com/ggerganov/llama.cpp.git && \
    cd llama.cpp && \
    cmake -B build && \
    cmake --build build --config Release && \
    mkdir -p build/bin && \
    if [ -f build/llama ]; then mv build/llama build/bin/llama; fi && \
    if [ -f build/bin/llama-cli ]; then ln -sf build/bin/llama-cli build/bin/llama; fi

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "ensemble.test_harness"]

# Note: Mount models/ as a volume when running the container
# Example: docker run -it -v $(pwd)/models:/app/models eidolon:latest 