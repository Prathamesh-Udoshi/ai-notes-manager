from transformers import pipeline

title_generator = pipeline("summarization", model="t5-small")

def generate_title(text: str) -> str:
    if not text or len(text.split()) < 5:
        return "Untitled Note"
    result = title_generator("summarize: " + text, max_length=10, min_length=3, do_sample=False)
    return result[0]["summary_text"]
