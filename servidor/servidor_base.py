from abc import ABC, abstractmethod
import requests
import time

class Servidor(ABC):

	def __init__(self, ejecutable, modelo, capas, contexto, host, puerto):
		self.ejecutable = ejecutable
		self.modelo = modelo
		self.capas = str(capas)
		self.contexto = str(contexto)
		self.host = host
		self.puerto = str(puerto)
		self.url = f"http://{host}:{puerto}"


	@abstractmethod
	def crear_proceso(self):
		pass


	def esta_disponible(self):
		try:
			respuesta = requests.get(
				f"{self.url}/v1/models",
				timeout=1
			)
			return respuesta.ok
		except requests.RequestException:
			return False


	def activar(self):
		proceso = self.crear_proceso()
		while proceso.poll() is None:
			if self.esta_disponible():
				return True
			time.sleep(0.5)
		return False