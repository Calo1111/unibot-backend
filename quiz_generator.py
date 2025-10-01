import openai

# Inserisci la tua API Key OpenAI
openai.api_key = "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"

def generate_quiz(topic):
    prompt = (
        f"Crea 5 domande a scelta multipla sull'argomento '{topic}'. "
        "Ogni domanda deve avere 4 opzioni e una sola risposta corretta. "
        "Indica la risposta corretta e spiega brevemente perché."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
