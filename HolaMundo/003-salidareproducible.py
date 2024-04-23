import json
import requests
import random

url = 'http://localhost:11434/api/generate'

# Establecer una semilla para que la generación de texto sea reproducible
random.seed(42)

while True:
    try:
        prompt = input("Ingrese su pregunta: ")
        data = {
            "model": "llama3",
            "prompt": prompt
        }

        response = requests.post(url, json=data)
        responses = []  # Lista para almacenar las respuestas en orden

        if response.status_code == 200:
            # Dividir la respuesta en líneas y procesar cada línea como JSON
            for line in response.text.splitlines():
                json_data = json.loads(line)
                responses.append(json_data["response"])  # Agrega la respuesta a la lista

            # Imprime todas las respuestas en orden
            print("".join(responses))
        else:
            print("Error:", response.status_code)
    
    except Exception as e:
        print("Ocurrió un error:", e)
    
    finally:
        # Liberar recursos
        if 'response' in locals():
            response.close()
