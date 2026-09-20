from servidor.servidor_base import Servidor
import subprocess

class ServidorLenguaje(Servidor):

	def crear_proceso(self):
		return subprocess.Popen([
			self.ejecutable,
			"-m", self.modelo,
			"-ngl", self.capas,
			"-c", self.contexto,
			"--host", self.host,
			"--port", self.puerto
		])