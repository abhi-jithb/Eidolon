#!/bin/bash
# 📦 Download recommended GGUF models for Eidolon

set -e

mkdir -p models
cd models || exit 1

# Mistral 7B Instruct
wget -nc https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf -O mistral.gguf

# Phi-2
wget -nc https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_0.gguf -O phi2.gguf

# TinyLlama
wget -nc https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_0.gguf -O tinyllama.gguf

# Qwen 1.5B
wget -nc https://huggingface.co/TheBloke/Qwen1.5-1B-Chat-GGUF/resolve/main/qwen1.5-1b-chat.Q4_0.gguf -O qwen.gguf

# Whisper model (optional, for STT)
wget -nc https://huggingface.co/ggerganov/whisper.cpp/resolve/main/models/ggml-base.en.bin -O ggml-base.en.bin

echo "✅ Models downloaded successfully. You can now run Eidolon using ./run.sh" 