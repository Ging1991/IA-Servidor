from servidor.servidor_base import Servidor
import subprocess

class ServidorEmbeddings(Servidor):

	def crear_proceso(self):
		return subprocess.Popen([
			self.ejecutable,
			"-m", self.modelo,
			"--embeddings",
			"--pooling", "mean",
			"-ngl", self.capas,
			"-c", self.contexto,
			"--host", self.host,
			"--port", self.puerto
		])