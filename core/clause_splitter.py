import re


def split_clauses(text):
    """
    Splits contract text into logical clauses using
    multiple legal formatting patterns.

    Designed to be:
    - PDF friendly
    - DOCX friendly
    - Robust for Indian & global contracts
    """

    if not text:
        return []

    # Normalize whitespace
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n{2,}", "\n", text)

    # Common legal clause boundaries
    clause_patterns = [
        r"\n\d+\.",                 # 1. 2. 3.
        r"\n\d+\)",                 # 1) 2)
        r"\n\([a-zA-Z]\)",          # (a) (b)
        r"\n\([ivx]+\)",            # (i) (ii)
        r"\n[A-Z][A-Z\s]{3,}:",     # TERMINATION:
        r"\n[A-Z][A-Z\s]{3,}\n",    # TERMINATION
        r"\n•",                     # Bullet points
        r"\n-",                     # Hyphen bullets
    ]

    split_regex = "|".join(clause_patterns)

    raw_clauses = re.split(split_regex, text)

    # Clean and filter clauses
    clauses = []
    for clause in raw_clauses:
        cleaned = clause.strip()

        # Ignore very short junk fragments
        if len(cleaned) < 40:
            continue

        clauses.append(cleaned)

    return clauses
