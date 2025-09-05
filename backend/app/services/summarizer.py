from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    if not text or len(text.split()) < 10:
        return "Text too short to summarize."
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
    return summary[0]["summary_text"]
