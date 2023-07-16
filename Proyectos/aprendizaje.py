import tensorflow as tf
import tensorflow_text as tf_text
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
 # Cargar el modelo pre-entrenado y el tokenizador
ruta_modelo_ajustado = "./modelo_ajustado"
modelo = TFGPT2LMHeadModel.from_pretrained("gpt2")
tokenizador = GPT2Tokenizer.from_pretrained("gpt2")
 # Texto de inicio
seed_text = "Hoy es un hermoso día"
 # Codificar el texto de inicio
input_ids = tokenizador.encode(seed_text, return_tensors="tf")
 # Generar texto con el modelo
output = modelo.generate(input_ids, max_length=100, num_return_sequences=1)
 # Decodificar el texto generado
generated_text = tokenizador.decode(output[0], skip_special_tokens=True)
print("Texto generado:", generated_text)
