from transformers import pipeline

# Load once at startup
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text: str) -> str:
    if not text or len(text.split()) < 10:
        return "Text too short to summarize."

    # Handle very long notes by splitting into chunks
    if len(text.split()) > 500:
        chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        summaries = []
        for chunk in chunks:
            summary = summarizer(
                chunk,
                max_length=120,
                min_length=30,
                do_sample=False,
                num_beams=6,
                length_penalty=2.0
            )
            summaries.append(summary[0]["summary_text"])
        final_text = " ".join(summaries)
        # Summarize the combined summaries again for precision
        summary = summarizer(
            final_text,
            max_length=80,
            min_length=25,
            do_sample=False,
            num_beams=6,
            length_penalty=2.0
        )
        return summary[0]["summary_text"]

    # Normal short/medium text
    summary = summarizer(
        text,
        max_length=120,       # allow enough space for abstraction
        min_length=30,        # prevent very short output
        do_sample=False,
        num_beams=6,          # wider search = more accurate
        length_penalty=2.0,   # penalize overly long summaries
        clean_up_tokenization_spaces=True
    )

    return summary[0]["summary_text"]
