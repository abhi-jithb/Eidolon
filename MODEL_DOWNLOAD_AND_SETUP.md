# Model Download and Setup Guide for Eidolon

This guide explains how to download and set up quantized .gguf language models (LLMs) for use with Eidolon. These models are required for running the ensemble system and other LLM-based features.

---

## 1. Where to Get GGUF Models
Most quantized .gguf models are hosted by TheBloke on Hugging Face. Recommended models:
- Mistral 7B Instruct
- Phi-2
- TinyLlama
- Qwen 1.5B

---

## 2. Downloading Models

### Option 1: Using wget (Recommended for CLI)
Run these commands from your project root:

```bash
mkdir -p models

# Mistral 7B Instruct (Q4_0 GGUF)
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf -O models/mistral.gguf

# Phi-2 (Q4_0 GGUF)
wget https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_0.gguf -O models/phi2.gguf

# TinyLlama (Q4_0 GGUF)
wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_0.gguf -O models/tinyllama.gguf

# Qwen 1.5B (Q4_0 GGUF)
wget https://huggingface.co/TheBloke/Qwen1.5-1B-Chat-GGUF/resolve/main/qwen1.5-1b-chat.Q4_0.gguf -O models/qwen.gguf
```

### Option 2: Manual Download from Hugging Face
1. Go to the model's Hugging Face page:
   - [Mistral 7B Instruct GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
   - [Phi-2 GGUF](https://huggingface.co/TheBloke/phi-2-GGUF)
   - [TinyLlama GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
   - [Qwen GGUF](https://huggingface.co/TheBloke/Qwen1.5-1B-Chat-GGUF)
2. Scroll to "Files and versions".
3. Click the `.gguf` file you want (e.g., `*.Q4_0.gguf`).
4. Click "Download".
5. Move the downloaded file into your `models/` folder.

---

## 3. Automated Download Script
You can use this script to fetch all recommended models at once:

```bash
# download_models.sh
#!/bin/bash
# 📦 Download recommended GGUF models for Eidolon

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
```

---

## 4. Example Folder Structure
```
eidolon/
├── models/
│   ├── mistral.gguf
│   ├── phi2.gguf
│   ├── tinyllama.gguf
│   └── qwen.gguf
```

---

## 5. References
- [TheBloke on Hugging Face](https://huggingface.co/TheBloke)
- [Mistral 7B Instruct GGUF](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF)
- [Phi-2 GGUF](https://huggingface.co/TheBloke/phi-2-GGUF)
- [TinyLlama GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Qwen GGUF](https://huggingface.co/TheBloke/Qwen1.5-1B-Chat-GGUF)

---

*Once your models are downloaded and placed in the `models/` folder, you are ready to run Eidolon's ensemble system!* 