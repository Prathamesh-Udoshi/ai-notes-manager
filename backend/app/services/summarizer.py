from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    if not text or len(text.split()) < 10:
        return "Text too short to summarize."
    
    summary = summarizer(
        text,
        max_length=50,        # slightly increased to allow full meaning
        min_length=15,        # ensures not too short
        do_sample=False,      # deterministic
        num_beams=4,          # beam search for precision
        length_penalty=1.0,   # balanced length
        clean_up_tokenization_spaces=True
    )
    return summary[0]["summary_text"]
