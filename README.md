# Eidolon: An Offline, Emotionally Intelligent AI Assistant

## Project Vision
Eidolon aims to be a fully offline, modular, and highly efficient AI assistant that can run on low-RAM devices (2–4 GB) including mobile phones and single-board computers. It will understand, converse, analyze emotions, learn from user interactions, and execute tasks—all while prioritizing privacy and resource efficiency.

---

## Objectives
- **Verbal Intelligence:** Understand and generate natural, context-aware language.
- **Emotional Awareness:** Detect and respond to user emotions (from text and voice).
- **Continuous Learning:** Adapt and evolve by learning from user interactions, storing knowledge efficiently.
- **Low Resource Usage:** Operate on devices with limited RAM and storage.
- **Offline/Private:** All processing and learning is local; no cloud dependency.
- **Extensible:** Modular design for easy addition of new features (vision, IoT, etc.).

---

## Core Features
1. **Wake Word Listener:** Passive trigger for hands-free activation.
2. **Speech-to-Text (STT):** Converts spoken input to text using lightweight models.
3. **Emotion Analyzer:** Detects sentiment and tone from both text and voice.
4. **Intent Parser & Context Memory:** Understands user intent and maintains context/memory.
5. **Memory Store:** Efficiently stores facts, conversation history, and emotional context.
6. **Task Executor:** Executes commands (e.g., open apps, fetch info, control devices).
7. **Text-to-Speech (TTS):** Converts responses to natural-sounding speech.
8. **User Interface:** CLI, mobile shell, or app-based interaction.

---

## System Architecture
```
[ Wake Word Listener ]
        ↓
[ Speech-to-Text (STT) ]
        ↓
[ Emotion Analyzer ]
        ↓
[ Prompt Builder (context + emotion) ]
        ↓
[ LLM (quantized, e.g., Phi-2, Mistral) ]
        ↓
[ Task Executor / Command Handler ]
        ↓
[ Text-to-Speech (TTS) ]
        ↓
[ Memory Store (SQLite/FAISS/JSON) ]
```

---

## Technology Stack
- **Language Models:** Quantized LLMs (Phi-2, Mistral, TinyLlama, etc.) via llama.cpp
- **STT:** Whisper.cpp, Vosk
- **TTS:** Coqui TTS, RHVoice, eSpeak-NG
- **Emotion Analysis:** EmoRoBERTa, DistilBERT, pyAudioAnalysis
- **Memory:** SQLite, FAISS (quantized), custom JSON stores
- **Scripting:** Python (core logic), Bash (launchers), C++ (llama.cpp, whisper.cpp)
- **UI:** CLI (initial), optional Flutter/React Native for mobile

---

## Research Focus Areas
- **Emotion Recognition:** Efficient, accurate emotion detection from text and audio on-device.
- **Prompt Engineering:** Best ways to inject emotional and memory context into LLM prompts.
- **Memory Compression:** Using quantized embeddings and vector DBs for long-term memory.
- **LLM Optimization:** Balancing model size, speed, and intelligence for low-RAM devices.
- **Continual Learning:** On-device fine-tuning and adaptation (LoRA, QLoRA, etc.).
- **Data Privacy:** Ensuring all data stays local and secure.

---

## Initial Milestones
1. **MVP Flow:**
   - Text input → Emotion detection → Prompt building → LLM response → Memory logging
2. **Voice Integration:**
   - Add STT (Whisper.cpp/Vosk) and TTS (Coqui/RHVoice)
3. **Command Execution:**
   - Map intents to system/API actions
4. **Memory & Learning:**
   - Implement efficient memory store and retrieval
5. **Mobile Optimization:**
   - Test and optimize for Android/low-RAM devices

---

## Folder Structure (Planned)
```
eidolon/
├── assistant/
│   ├── main.py
│   ├── prompt_builder.py
│   ├── emotion.py
│   ├── memory.py
│   ├── executor.py
├── models/
├── audio/
├── data/
├── ui/
├── run.sh
└── README.md
```

---

## Contribution & Roadmap
- **Open to contributions:** Research, code, optimization, and testing.
- **Roadmap:**
  - [ ] MVP CLI assistant
  - [ ] Voice input/output
  - [ ] Emotion-aware responses
  - [ ] Efficient memory/learning
  - [ ] Mobile deployment

---

## References & Further Reading
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Whisper.cpp](https://github.com/ggerganov/whisper.cpp)
- [Coqui TTS](https://github.com/coqui-ai/TTS)
- [FAISS](https://github.com/facebookresearch/faiss)
- [LoRA: Low-Rank Adaptation of LLMs](https://arxiv.org/abs/2106.09685)
- [Emotion Recognition Papers](https://paperswithcode.com/task/emotion-recognition)

---

*Eidolon is a research-driven, privacy-first project. The goal is to push the boundaries of what's possible with on-device AI assistants.* 