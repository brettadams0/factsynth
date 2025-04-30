# core/claim_handler.py
# 🧠 Cleans and normalizes input claims for processing

import re


def clean_claim(claim):
    """
    Normalize and clean a raw claim string.
    Removes excessive punctuation, standardizes spacing, etc.
    """
    cleaned = claim.strip()
    cleaned = re.sub(r'\s+', ' ', cleaned)              # Remove extra spaces
    cleaned = re.sub(r'["\']', '', cleaned)             # Remove quotes
    cleaned = re.sub(r'[?!.]+$', '', cleaned)            # Remove trailing punctuation
    cleaned = cleaned.capitalize()
    print(f"✅ Normalized Claim: \"{cleaned}\"")
    return cleaned
