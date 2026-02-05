from langdetect import detect
from deep_translator import GoogleTranslator


# -------------------- LANGUAGE DETECTION --------------------
def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "unknown"


# -------------------- INPUT NORMALIZATION --------------------
def normalize_to_english(text, llm=None):
    """
    Detects input language and normalizes text to English
    for internal legal analysis.
    """
    lang = detect_language(text)

    if lang == "en":
        return text, "en"

    # Optional LLM-based translation
    if llm:
        prompt = f"Translate the following legal text to English:\n{text}"
        translated = llm(prompt)
        return translated, lang

    # Fallback: deep-translator
    try:
        translated = GoogleTranslator(source="auto", target="en").translate(text)
        return translated, lang
    except Exception:
        return text, lang


# -------------------- OUTPUT TRANSLATION --------------------
def translate_output(text, target_lang="en"):
    """
    Translates analysis output into the user-selected language.
    """
    if not text or target_lang == "en":
        return text

    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception:
        return text
