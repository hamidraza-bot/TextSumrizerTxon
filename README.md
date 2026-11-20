# TXON_01 - Basic Prompting & Text Summarizer

**TXON AI Engineer Internship - Level 01, Week 01, Task 01**

A beginner-friendly Python script that takes a text article (from the console,
inline, or a `.txt` file) and uses an AI API to produce:

- a one-sentence **summary**
- exactly **3 bullet-point key takeaways**

Supports **OpenAI** (`gpt-4o-mini`) and **Hugging Face Inference API**.

## Features
- Input from console, `--text`, or a local `.txt` file
- System + user prompt design that forces a strict output format
- Clean, formatted terminal output
- Optional save to an output file
- Switch between OpenAI and Hugging Face with one flag
- Basic error handling (missing file, missing key, API failure)

## Project Structure
```
TXON_01/
|-- summarizer.py       # main script
|-- sample_article.txt  # example input
|-- requirements.txt    # dependencies
|-- .env.example        # template for API keys
|-- .gitignore
`-- README.md
```

## Setup
1. Install Python 3.9+
2. (Optional) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create your key file:
   ```bash
   cp .env.example .env          # Windows: copy .env.example .env
   ```
   Open `.env` and paste your key:
   - OpenAI key: https://platform.openai.com/api-keys
   - Hugging Face token (free): https://huggingface.co/settings/tokens

## Usage
```bash
# Summarize a text file (OpenAI)
python summarizer.py --file sample_article.txt

# Save the result to a file
python summarizer.py --file sample_article.txt --output output.txt

# Use the free Hugging Face API
python summarizer.py --file sample_article.txt --provider huggingface

# Inline text
python summarizer.py --text "Paste your short article here..."

# Interactive console mode (paste text, then type END)
python summarizer.py
```

### Example output
```
============================================================
  TXON TEXT SUMMARIZER
============================================================
  Provider : openai (gpt-4o-mini)
  Input    : 142 words
============================================================

SUMMARY: AI tools are boosting productivity and learning, but need careful use.

KEY TAKEAWAYS:
- Language models help draft, summarize, and answer questions.
- AI can make mistakes, so outputs must be verified.
- Hands-on projects are the best way for beginners to learn AI.
============================================================
```

## How It Works (Code Flow)
1. `parse_args()` reads CLI options.
2. `get_input_text()` loads text from file / argument / console.
3. `summarize()` sends the **system prompt** (format rules) and **user prompt**
   (the text) to the chosen API.
4. `format_output()` builds a clean report, which is printed and optionally saved.

## Prompt Structure
- **System prompt:** defines the role and the exact output format (1 summary
  sentence + 3 bullets, under 25 words each, no outside information).
- **User prompt:** wraps the article text and asks for a summary.
- `temperature=0.3` keeps the output focused and consistent.

## Tech Stack
Python, OpenAI API, Hugging Face Inference API, python-dotenv, basic file I/O

## Author
Your Name - TXON AI Engineer Intern
