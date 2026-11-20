#!/usr/bin/env python3
"""
TXON AI Engineer Internship - Task 01
Basic Prompting & Text Summarizer

Takes text from the console, a --text argument, or a .txt file and uses an
AI API (OpenAI or Hugging Face) to produce a short summary plus exactly
3 bullet-point takeaways. Output is printed and can be saved to a file.
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # reads API keys from the .env file

# ----------------------------------------------------------------------------
# Prompts
# ----------------------------------------------------------------------------
SYSTEM_PROMPT = (
    "You are a precise summarization assistant. "
    "You read the text given by the user and respond ONLY in this exact format:\n\n"
    "SUMMARY: <one clear sentence summarizing the whole text>\n\n"
    "KEY TAKEAWAYS:\n"
    "- <takeaway 1>\n"
    "- <takeaway 2>\n"
    "- <takeaway 3>\n\n"
    "Rules: exactly 3 bullet points, each under 25 words, plain language, "
    "no information that is not in the text."
)

USER_PROMPT_TEMPLATE = "Summarize the following text:\n\n\"\"\"\n{text}\n\"\"\""

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "huggingface": "meta-llama/Llama-3.1-8B-Instruct",
}

MAX_CHARS = 12000  # keep requests small and cheap for beginners


# ----------------------------------------------------------------------------
# Input handling
# ----------------------------------------------------------------------------
def read_from_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.is_file():
        sys.exit(f"[Error] File not found: {path}")
    return file_path.read_text(encoding="utf-8").strip()


def read_from_console() -> str:
    print("Paste your text below. Type END on a new line (or press Ctrl+D) to finish:\n")
    lines = []
    try:
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
    except EOFError:
        pass
    return "\n".join(lines).strip()


def get_input_text(args) -> str:
    if args.file:
        return read_from_file(args.file)
    if args.text:
        return args.text.strip()
    return read_from_console()


# ----------------------------------------------------------------------------
# AI providers
# ----------------------------------------------------------------------------
def summarize_openai(text: str, model: str) -> str:
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("[Error] OPENAI_API_KEY missing. Add it to your .env file.")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)},
        ],
        temperature=0.3,
        max_tokens=300,
    )
    return response.choices[0].message.content.strip()


def summarize_huggingface(text: str, model: str) -> str:
    from huggingface_hub import InferenceClient

    token = os.getenv("HF_API_KEY")
    if not token:
        sys.exit("[Error] HF_API_KEY missing. Add it to your .env file.")

    client = InferenceClient(api_key=token)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_TEMPLATE.format(text=text)},
        ],
        temperature=0.3,
        max_tokens=300,
    )
    return response.choices[0].message.content.strip()


def summarize(text: str, provider: str, model: str) -> str:
    if provider == "openai":
        return summarize_openai(text, model)
    return summarize_huggingface(text, model)


# ----------------------------------------------------------------------------
# Output handling
# ----------------------------------------------------------------------------
def format_output(summary: str, provider: str, model: str, word_count: int) -> str:
    line = "=" * 60
    return (
        f"{line}\n"
        f"  TXON TEXT SUMMARIZER\n"
        f"{line}\n"
        f"  Provider : {provider} ({model})\n"
        f"  Input    : {word_count} words\n"
        f"  Time     : {datetime.now():%Y-%m-%d %H:%M:%S}\n"
        f"{line}\n\n"
        f"{summary}\n\n"
        f"{line}\n"
    )


def save_output(content: str, path: str) -> None:
    Path(path).write_text(content, encoding="utf-8")
    print(f"[Saved] Summary written to {path}")


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def parse_args():
    parser = argparse.ArgumentParser(
        description="Summarize text into a short summary + 3 bullet takeaways."
    )
    parser.add_argument("-f", "--file", help="Path to a .txt file to summarize")
    parser.add_argument("-t", "--text", help="Text to summarize (inline)")
    parser.add_argument("-o", "--output", help="Save the result to this file")
    parser.add_argument(
        "-p", "--provider", choices=["openai", "huggingface"], default="openai",
        help="AI provider to use (default: openai)",
    )
    parser.add_argument("-m", "--model", help="Override the default model name")
    return parser.parse_args()


def main():
    args = parse_args()
    model = args.model or DEFAULT_MODELS[args.provider]

    text = get_input_text(args)
    if not text:
        sys.exit("[Error] No text provided.")
    if len(text) > MAX_CHARS:
        print(f"[Warning] Text is long, truncating to {MAX_CHARS} characters.")
        text = text[:MAX_CHARS]

    print(f"[Info] Summarizing with {args.provider} / {model} ...\n")
    try:
        summary = summarize(text, args.provider, model)
    except Exception as exc:  # API errors, network issues, bad key, etc.
        sys.exit(f"[Error] API request failed: {exc}")

    result = format_output(summary, args.provider, model, len(text.split()))
    print(result)

    if args.output:
        save_output(result, args.output)


if __name__ == "__main__":
    main()
