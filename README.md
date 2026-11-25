# AI Text Summarizer — TXON Internship Task 01 📝

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-gpt--4o--mini-412991?style=flat-square&logo=openai&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Llama--3.1--8B-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)

**TXON AI Engineer Internship — Level 01, Week 01, Task 01**

A beginner-friendly Python CLI that takes a text article (from the console, inline, or a `.txt` file) and uses an AI API to produce a **one-sentence summary** plus exactly **3 bullet-point key takeaways**.

Supports **OpenAI** (`gpt-4o-mini`) and the **Hugging Face Inference API** (`meta-llama/Llama-3.1-8B-Instruct`).

## ✨ Features

- 📥 Input from console, `--text`, or a local `.txt` file
- 🎯 System + user prompt design that forces a strict output format
- 🧹 Clean, formatted terminal output (provider, model, word count, timestamp)
- 💾 Optional save to an output file
- 🔀 Switch between OpenAI and Hugging Face with one flag
- 🛡️ Basic error handling (missing file, missing key, API failure)
- 💰 Input capped at 12,000 characters to keep requests small and cheap

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.9+ |
| AI providers | OpenAI API, Hugging Face Inference API |
| Config | `python-dotenv` (`.env` file for API keys) |
| CLI | `argparse` (standard library) |

## 🚀 Setup

1. Install **Python 3.9+**.
2. (Optional) Create a virtual environment:

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

   Open `.env` and paste your key(s):
   - **OpenAI key:** https://platform.openai.com/api-keys
   - **Hugging Face token (free):** https://huggingface.co/settings/tokens

## 💻 Usage

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

## ⚙️ How It Works

1. `parse_args()` reads the CLI options (`--file`, `--text`, `--provider`, `--model`, `--output`).
2. `get_input_text()` loads the article from a file, inline text, or the console.
3. A strict **system prompt** forces the model to reply only in the `SUMMARY:` + `KEY TAKEAWAYS:` format (exactly 3 bullets, each under 25 words, no invented information).
4. `summarize_openai()` or `summarize_huggingface()` calls the chosen provider.
5. `format_output()` prints the result; `save_output()` optionally writes it to a file.

## 📁 Project Structure

```
├── summarizer.py       # Main script
├── sample_article.txt  # Example input
├── requirements.txt    # Dependencies (openai, huggingface_hub, python-dotenv)
├── .env.example        # Template for API keys (copy to .env)
├── .gitignore
├── README.md
└── LICENSE
```

> **Note:** `_.env.example` and `_.gitignore` are legacy copies from the original upload (GitHub's web uploader hid dotfiles). The canonical files are now `.env.example` and `.gitignore`.

## 📄 License

MIT — see [LICENSE](LICENSE).

---

Built by [Hamid Raza](https://github.com/hamidraza-bot) · AI Automation Engineer · [Fiverr](https://www.fiverr.com/hamid_buildai)
