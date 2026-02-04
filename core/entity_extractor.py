import re

def extract_entities(text):
    """
    Lightweight NER using regex and heuristics.
    Suitable for contracts and legal text.
    """

    entities = {
        "parties": [],
        "dates": [],
        "amounts": [],
        "jurisdiction": [],
        "duration": []
    }

    # --- Parties (very basic heuristic) ---
    party_patterns = [
        r"between\s+([A-Z][A-Za-z\s&]+)\s+and\s+([A-Z][A-Za-z\s&]+)",
        r"this agreement is made by\s+([A-Z][A-Za-z\s&]+)"
    ]

    for p in party_patterns:
        matches = re.findall(p, text, flags=re.IGNORECASE)
        for m in matches:
            if isinstance(m, tuple):
                entities["parties"].extend([x.strip() for x in m])
            else:
                entities["parties"].append(m.strip())

    # --- Dates ---
    date_pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b"
    entities["dates"] = re.findall(date_pattern, text)

    # --- Money / Amounts ---
    money_pattern = r"(₹|\$|Rs\.?)\s?\d+(?:,\d+)*(?:\.\d+)?"
    entities["amounts"] = re.findall(money_pattern, text)

    # --- Jurisdiction ---
    jurisdiction_keywords = [
        "governed by the laws of",
        "jurisdiction of",
        "courts at"
    ]

    for line in text.split("\n"):
        for key in jurisdiction_keywords:
            if key in line.lower():
                entities["jurisdiction"].append(line.strip())

    # --- Duration ---
    duration_pattern = r"\b\d+\s+(years?|months?)\b"
    entities["duration"] = re.findall(duration_pattern, text, flags=re.IGNORECASE)

    return entities
