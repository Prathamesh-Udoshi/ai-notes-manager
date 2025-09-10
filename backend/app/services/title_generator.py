import nltk
nltk.download('stopwords')
from transformers import pipeline
from rake_nltk import Rake

# Load BART in text2text-generation
title_gen = pipeline("text2text-generation", model="facebook/bart-large-cnn")

def generate_keywords(text: str, num_keywords: int = 3):
    """Extract top keywords using RAKE"""
    rake = Rake()
    rake.extract_keywords_from_text(text)
    key_phrases = rake.get_ranked_phrases()
    return key_phrases[:num_keywords]

def generate_title(text: str) -> str:
    if not text or len(text.split()) < 5:
        return "Untitled Note"

    # Extract keywords to guide BART
    keywords = generate_keywords(text)
    keywords_str = ", ".join(keywords)

    # Stronger prompt to avoid copying
    prompt = (
        "Write a short, creative, and original 4 to 6 word title (not copied from the text, "
        "no starting with the same words, headline style) based on this note. "
        f"Focus on the theme and keywords: {keywords_str}. "
        f"\n\nNote:\n{text}\n\nSmart Title:"
    )

    try:
        result = title_gen(
            prompt,
            max_length=12,
            min_length=4,
            num_beams=10,
            no_repeat_ngram_size=3,
            early_stopping=True
        )
        title = result[0]["generated_text"].strip()

        # Remove "Title:" if echoed
        if title.lower().startswith("smart title:"):
            title = title.split(":", 1)[1].strip()

        # Capitalize each word
        title = " ".join(word.capitalize() for word in title.split())

        # Ensure it’s not just the first line of text
        if text.lower().startswith(title.lower()):
            title = " ".join(keywords).title()

        return title if title else "Untitled Note"

    except Exception as e:
        print("Title generation failed:", e)
        return "Untitled Note"
