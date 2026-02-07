# Mental Health Support Chatbot 🧠

A compassionate AI chatbot designed to provide mental health support, positive affirmations, and guided meditations. Built with [Streamlit](https://streamlit.io/) and powered by local LLMs via [Ollama](https://ollama.com/).

## Features

- **Empathetic Chat Interface**: Have open-ended conversations for support and guidance.
- **Daily Affirmations**: Generate positive affirmations to boost your mood.
- **Guided Meditations**: Receive personalized mindfulness meditation scripts.
- **Privacy-Focused**: Runs completely locally on your machine using Ollama.
- **Customizable Interface**: Clean UI with a calming background.

## Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.8+**
2.  **[Ollama](https://ollama.com/)**: This application requires Ollama to run the language model locally.

## Installation

1.  **Clone the repository** (or download the files to a directory):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install Python dependencies**:
    ```bash
    pip install streamlit ollama
    ```

3.  **Set up Ollama**:
    - Download and install Ollama from [ollama.com](https://ollama.com/).
    - Pull the default model (TinyLlama):
      ```bash
      ollama pull tinyllama
      ```
    - *Note: You can use other models like `llama3`, `phi3`, etc., by changing the `OLLAMA_MODEL` variable in `mental_support.py`.*

## Usage

1.  **Ensure Ollama is running** in the background.

2.  **Run the Streamlit app**:
    ```bash
    streamlit run mental_support.py
    ```

3.  The application will open in your default web browser at `http://localhost:8501`.

## Configuration

### Changing the Model
To use a different model (e.g., `llama3` or `phi3`):
1.  Open `mental_support.py`.
2.  Locate the line:
    ```python
    OLLAMA_MODEL = "tinyllama"
    ```
3.  Change `"tinyllama"` to your preferred model tag.
4.  Make sure you have pulled that model using `ollama pull <model_name>`.

### Custom Background
The app looks for a file named `background.png` in the same directory. You can replace this file with any image you prefer to customize the look.

## Disclaimer
*This chatbot is an AI tool and is not a substitute for professional mental health advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.*
