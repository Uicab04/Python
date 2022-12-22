import os
import openai

openai.api_key = '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'

conversation = "HOLA QUE TAL?"
i = 1
while (i != 0):
  question = input("Humano: ")
  conversation += "The following is a conversation with an AI assistant. The assistant is very fun, optimistic, helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHumano: " + question + "\nAI:"
  response = openai.Completion.create(
    model="davinci",
    prompt=conversation,
    temperature=0.5,
    max_tokens=150,
    top_p=0.3,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["\n", " Humano:", " AI:"]
  )
  anwer = response.choices[0].text.strip()
  conversation += anwer
  print("AI: " + anwer + "\n")