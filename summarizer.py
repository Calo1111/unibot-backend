import fitz  # PyMuPDF
import openai

# Inserisci la tua API Key OpenAI
openai.api_key = "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"

def summarize_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()


    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Riassumi questo testo universitario:\n{text}"}
        ]
    )
    return response.choices[0].message.content
