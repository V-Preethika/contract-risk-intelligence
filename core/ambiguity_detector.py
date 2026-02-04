AMBIGUOUS_PHRASES = [
    "reasonable efforts",
    "best efforts",
    "from time to time",
    "as soon as practicable",
    "sole discretion",
    "materially",
    "substantially",
    "as may be agreed"
]

def detect_ambiguity(clauses):
    """
    Flags clauses containing ambiguous language.
    """

    ambiguous_clauses = []

    for clause in clauses:
        for phrase in AMBIGUOUS_PHRASES:
            if phrase in clause.lower():
                ambiguous_clauses.append({
                    "phrase": phrase,
                    "clause": clause
                })
                break

    return ambiguous_clauses
