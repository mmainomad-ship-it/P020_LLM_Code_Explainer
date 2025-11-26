# P020 - Local LLM Code Explainer

## Description
A Python tool that reads a local code file and uses a local LLM (Ollama) to provide a clear, non-technical explanation of the logic. It acts as an automated documentation assistant.

## Key Features
- **File Parsing**: Safely reads Python source files.
- **Local AI Analysis**: Uses Ollama (Llama 3 or similar) for privacy and zero cost.
- **Beginner Friendly**: Prompts the AI to act as a Senior Instructor.

## Technology Stack
- Python 3.x
- Requests Library (API connection)
- Ollama (Local LLM)

## Setup
1. Install Ollama and pull a model (e.g., `ollama pull llama3`).
2. Run `pip install -r requirements.txt`.
3. Run `python explainer.py`.

## Author
**mmainomad-ship-it**
[GitHub Profile](https://github.com/mmainomad-ship-it)