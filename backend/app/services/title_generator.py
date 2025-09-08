from transformers import pipeline

title_generator = pipeline("text2text-generation", model="t5-small")

def generate_title(text: str) -> str:
    if not text or len(text.split()) < 5:
        return "Untitled Note"
    
    # Instead of summarization, explicitly ask the model to "generate a title"
    prompt = "generate a creative title: " + text
    
    result = title_generator(prompt, max_length=12, min_length=3, do_sample=False)
    return result[0]["generated_text"]
