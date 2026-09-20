import os

ANSI_INICIO = "\033["
ANSI_RESET = "\033[0m" 
ROJO = "31m"
VERDE = "32m"
AMARILLO = "33m"

def inicializar():
	os.system('')

def escribir_rojo(texto):
	print(f"{ANSI_INICIO}{ROJO}{texto}{ANSI_RESET}")

def escribir_verde(texto):
	print(f"{ANSI_INICIO}{VERDE}{texto}{ANSI_RESET}")

def escribir_amarillo(texto):
	print(f"{ANSI_INICIO}{AMARILLO}{texto}{ANSI_RESET}")