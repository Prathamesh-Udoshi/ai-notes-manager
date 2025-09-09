from transformers import pipeline

# Use T5-base for better generation quality
title_generator = pipeline("text2text-generation", model="t5-base")

def generate_title(text: str) -> str:
    if not text or len(text.split()) < 5:
        return "Untitled Note"
    
    # Stronger instruction prompt
    prompt = (
        "Write a short, catchy, and relevant title (max 8 words) "
        "for the following note:\n\n"
        f"{text}\n\nTitle:"
    )

    result = title_generator(
        prompt,
        max_length=15,        # keep it short
        min_length=3,
        num_beams=6,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    title = result[0]["generated_text"].strip()

    # Extra cleanup: remove "Title:" prefix if model includes it
    if title.lower().startswith("title:"):
        title = title[6:].strip()

    # Fallback if junk or empty
    if not title or len(title.split()) < 2:
        title = "Untitled Note"

    return title
