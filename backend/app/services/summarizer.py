from transformers import pipeline

# Load summarizer once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    if not text or len(text.split()) < 10:
        return text if text else "Text too short to summarize."

    try:
        summary = summarizer(
            text,
            max_length=80,       # balanced length
            min_length=25,        # avoid too short
            do_sample=False,
            num_beams=6,
            length_penalty=2.0
        )
        return summary[0]["summary_text"].strip()
    except Exception as e:
        print("Summarization failed:", e)
        return text[:150] + "..." if len(text) > 150 else text
