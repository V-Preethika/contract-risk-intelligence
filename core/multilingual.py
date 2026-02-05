from langdetect import detect
from deep_translator import GoogleTranslator

# Initialize translator once
translator = Translator()


# -------------------- LANGUAGE DETECTION --------------------
def detect_language(text):
    try:
        return detect(text)
    except:
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

    # If an LLM is provided, use it for translation
    if llm:
        prompt = f"Translate the following legal text to English:\n{text}"
        translated = llm(prompt)
        return translated, lang

    # Fallback: return original text if no translator is configured
    return text, lang


# -------------------- OUTPUT TRANSLATION --------------------
def translate_output(text, target_lang="en"):
    return GoogleTranslator(source="auto", target=target_lang).translate(text)

    """
    Translates analysis output (summary, explanations, clauses)
    into the user-selected language.

    Handles long legal text safely by chunking to avoid
    googletrans silent failures.
    """

    if not text or target_language.lower() == "english":
        return text

    # LLM-based translation (future / production-ready)
    if llm:
        prompt = f"Translate the following text into {target_language}:\n{text}"
        return llm(prompt)

    # Supported language mapping (googletrans codes)
    language_map = {
        "hindi": "hi",
        "tamil": "ta",
        "telugu": "te",
        "kannada": "kn",
        "malayalam": "ml",
        "marathi": "mr",
        "bengali": "bn",
        "gujarati": "gu",
        "urdu": "ur",
        "spanish": "es",
        "french": "fr",
        "german": "de"
    }

    lang_key = target_language.lower()
    if lang_key not in language_map:
        return text

    try:
        # 🔹 Split long legal text into smaller chunks
        chunks = []
        current = ""

        for sentence in text.split(". "):
            if len(current) + len(sentence) < 400:
                current += sentence + ". "
            else:
                chunks.append(current.strip())
                current = sentence + ". "

        if current:
            chunks.append(current.strip())

        # 🔹 Translate each chunk safely
        translated_chunks = []
        for chunk in chunks:
            translated = translator.translate(
                chunk,
                dest=language_map[lang_key]
            ).text
            translated_chunks.append(translated)

        return " ".join(translated_chunks)

    except Exception:
        return text
