#!/bin/bash
# Eidolon local setup script
set -e

# Clone and build llama.cpp if not present
if [ ! -d "llama.cpp" ]; then
  echo "Cloning llama.cpp..."
  git clone https://github.com/ggerganov/llama.cpp.git
fi
cd llama.cpp && make && cd ..

# Install Python dependencies
if command -v pip3 &>/dev/null; then
  PIP=pip3
else
  PIP=pip
fi
$PIP install -r requirements.txt

# Print next steps
cat <<EOF

✅ Local setup complete!
- Make sure your models are in the models/ directory.
- Edit config.yaml if needed (llama_cpp_path: llama.cpp/main).
- Run: python3 ensemble/test_harness.py
EOF 