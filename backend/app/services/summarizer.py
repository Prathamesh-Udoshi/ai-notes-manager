from transformers import pipeline

# Lazy load summarizer with lighter model
_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        # Use a lighter model for less memory usage
        _summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    return _summarizer

def generate_summary(text: str) -> str:
    if not text or len(text.split()) < 10:
        return text if text else "Text too short to summarize."

    try:
        summarizer = get_summarizer()
        summary = summarizer(
            text,
            max_length=80,
            min_length=25,
            do_sample=False,
            num_beams=6,
            length_penalty=2.0
        )
        return summary[0]["summary_text"].strip()
    except Exception as e:
        print("Summarization failed:", e)
        return text[:150] + "..." if len(text) > 150 else text
