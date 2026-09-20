import requests

def generar_respuesta(url, contenido):
	payload = {
		"messages": [
			{
				"role": "user",
				"content": contenido
			}
		]
	}

	respuesta = requests.post(
		f"{url}/v1/chat/completions",
		json=payload,
		timeout=120
	)

	respuesta.raise_for_status()
	datos = respuesta.json()
	return datos["choices"][0]["message"]["content"]


def generar_embedding(url, contenido):
	payload = {
		"input": contenido
	}

	respuesta = requests.post(
		f"{url}/v1/embeddings",
		json=payload,
		timeout=120
	)

	respuesta.raise_for_status()
	datos = respuesta.json()
	return datos["data"][0]["embedding"]