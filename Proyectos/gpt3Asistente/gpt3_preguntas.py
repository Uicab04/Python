import os
import openai

openai.api_key = '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'

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
question = "quienes somos?"
response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Soy un bot de respuesta a preguntas muy inteligente. Si me haces una pregunta que tiene sus raíces en la verdad, te daré la respuesta. Si me hace una pregunta que es una tontería, un engaño o que no tiene una respuesta clara, le responderé con \"Desconocido\".\n\nQ: "+ question +" \nA:",
  temperature=0,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\n"]
)


print(response.choices[0].text.strip())