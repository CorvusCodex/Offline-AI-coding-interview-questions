#!/usr/bin/env python3
"""
Coding Interview Question Generator (offline)
Usage:
  python main.py --input "Topic: Python data structures; Level: medium"
"""
import argparse, requests, os, sys, re

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 180

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(spec):
    return (
        "Generate 5 coding interview questions for the given topic and difficulty.\n"
        "For each question include a brief answer hint (1-2 sentences).\n\n"
        f"{spec}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True)
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
