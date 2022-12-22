import os
import openai


openai.api_key = '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'

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="hola diego",
  temperature=0.7,
  max_tokens=700,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


print(response.choices[0].text.strip())