import json
import requests

url = 'http://localhost:11434/api/generate'

while True:
    prompt = input("Ingrese su pregunta: ")
    data = {
        "model": "llama3",
        "prompt": prompt
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        responses = []  # Lista para almacenar las respuestas en orden
        # Dividir la respuesta en líneas y procesar cada línea como JSON
        for line in response.text.splitlines():
            json_data = json.loads(line)
            responses.append(json_data["response"])  # Agrega la respuesta a la lista

        # Imprime todas las respuestas en orden
        print("".join(responses))
    else:
        print("Error:", response.status_code)