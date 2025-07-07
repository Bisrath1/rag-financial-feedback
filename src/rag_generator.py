from transformers import pipeline
from prompt_template import format_prompt

# Load the generation model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(question, context_chunks):
    prompt = format_prompt(question, context_chunks)
    result = generator(prompt, max_length=512, do_sample=False)
    return result[0]['generated_text']
