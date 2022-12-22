
import openai
import requests

# Tu clave de API de OpenAI va aquí
openai.api_key = "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"

# Establecemos el modelo que queremos utilizar (en este caso, GPT-3)
model_engine = "text-davinci-002"

# Creamos la solicitud a la API de OpenAI
response = openai.Completion.create(
    engine=model_engine,
    prompt="¿realiza una introduccion a la programacion movil?",
    max_tokens=2048,
    n=1,
    temperature=0.5,
)

# Procesamos la respuesta
response_text = response["choices"][0]["text"]
print(response_text)


