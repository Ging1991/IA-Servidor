import json
from servidor.servidor_embeddings import ServidorEmbeddings
from servidor.servidor_lenguaje import ServidorLenguaje
import servidor.consola_color as consola
import servidor.pruebas_servidor as pruebas
import servidor.llamadas as llamadas

CONFIGURACION = "configuracion.json"
MENU = """Bienvenido al programa de asistencia para levantar servidores de modelos de IA.
Seleccione una de las siguientes opciones por favor.
1 - Levantar servidor de llm.
2 - Levantar servidor de embeddings.
3 - Realizar la prueba de verificación para el servidor de llm.
4 - Realizar la prueba de verificación para el servidor de embeddings.
5 - Realiza una pregunta directa al llm.
"""

def iniciar_servidor(servidor, tipo):
	if servidor.esta_disponible():
		consola.escribir_verde(f"[CORRECTO] El servidor de {tipo} ya estaba iniciado.")
		consola.escribir_amarillo("Puede cerrar esta ventana sin problemas.")
		input("Presione ENTER para continuar...")
		return
		
	consola.escribir_amarillo(f"Iniciando servidor de {tipo}...\n")

	if servidor.activar():
		consola.escribir_verde("\n[CORRECTO] Servidor listo.")
		consola.escribir_amarillo("[ADVERTENCIA] No cierre esta ventana mientras utiliza el sistema IA.")
	else:
		consola.escribir_rojo("[ERROR]: No se pudo iniciar el servidor.")

if __name__ == "__main__":
	consola.inicializar()

	with open(CONFIGURACION, "r", encoding="utf-8") as archivo:
		configuracion = json.load(archivo)

	ejecutable = configuracion["ejecutable"]
	host = configuracion["host"]
	contexto = configuracion["contexto"]
	capas = configuracion["capas"]
	modelo_lenguaje = configuracion["modelo_lenguaje"]
	modelo_embeddings = configuracion["modelo_embeddings"]
	puerto_lenguaje = configuracion["puerto_lenguaje"]
	puerto_embeddings = configuracion["puerto_embeddings"]
	url_lenguaje = f"http://{host}:{puerto_lenguaje}"
	url_embeddings = f"http://{host}:{puerto_embeddings}"

	print(MENU)
	opcion = int(input("Opción:"))

	if (opcion == 1):
		iniciar_servidor(ServidorLenguaje(ejecutable, modelo_lenguaje, capas, contexto, host, puerto_lenguaje), "llm")
	elif (opcion == 2):
		iniciar_servidor(ServidorEmbeddings(ejecutable, modelo_embeddings, capas, contexto, host, puerto_embeddings), "embeddings")
	elif (opcion == 3):
		pruebas.prueba_de_humo_llm(url_lenguaje)
	elif (opcion == 4):
		pruebas.prueba_de_humo_embeddings(url_embeddings)
	elif (opcion == 5):
		pregunta = input("Tu pregunta:")
		consola.escribir_verde(llamadas.generar_respuesta(url_lenguaje, pregunta))
	else:
		print("Opción no reconocida")