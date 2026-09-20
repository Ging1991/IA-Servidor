import requests
import servidor.consola_color as consola
import servidor.llamadas as llamadas

def prueba_de_humo_embeddings(url):
	try:
		consola.escribir_amarillo(f"Intentando conectar al servidor de embeddings en: {url}")
		vector = llamadas.generar_embedding(url, "Prueba de humo para embeddings")
		
		if isinstance(vector, list) and len(vector) > 0:
			consola.escribir_verde(f"PRUEBA EXITOSA: Se generó un vector con una dimensión de {len(vector)} valores.")
			consola.escribir_verde(f"Primeros valores del vector: {vector[:3]}...")
			return True
		else:
			consola.escribir_rojo("ERROR: El servidor respondió, pero el formato del vector no es válido.")
			return False

	except requests.exceptions.ConnectionError:
		consola.escribir_rojo("Error de conexión: No se pudo conectar al servidor de embeddings.")
		return False
	except requests.exceptions.Timeout:
		consola.escribir_rojo("Error: El servidor de embeddings tardó demasiado en responder (Timeout).")
		return False
	except Exception as e:
		consola.escribir_rojo(f"Error inesperado durante la prueba de embeddings: {e}")
		return False

def prueba_de_humo_llm(url):
	try:
		consola.escribir_amarillo(f"Intentando conectar al servidor de llm en: {url}...")
		respuesta = llamadas.generar_respuesta(url, "Responde únicamente con la palabra: OK")
		consola.escribir_verde(f"ÉXITO: El servidor de llm respondió: {respuesta.strip()}")
		return True
	except requests.exceptions.ConnectionError:
		consola.escribir_rojo("Error de conexión: No se pudo conectar al servidor de llm.")
		return False
	except requests.exceptions.Timeout:
		consola.escribir_rojo("Error: El servidor de llm tardó demasiado en responder (Timeout).")
		return False
	except Exception as e:
		consola.escribir_rojo(f"Error inesperado durante la prueba de llm: {e}")
		return False