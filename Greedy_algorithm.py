import heapq
import numpy as np

instancia = np.genfromtxt("Instancias.csv", delimiter = ",")

class Scheduling_jobs:
	"""
		Clase para la programación de trabajos
	"""

	def __init__(self, datos, opcion):

		# Datos con los que trabajar
		self.datos = datos
		
		# Cola de prioridad para el orden
		self.cola_prioridad = []

		# Agregar los datos en la priority queue
		for tarea in range(len(self.datos)):
			duracion = datos[tarea, 1] - datos[tarea, 0]
			inicio = datos[tarea, 0]

			if opcion == "prioridad_inicio":
				# prioridad basado en el inicio de la tarea
				heapq.heappush(self.cola_prioridad, (inicio, duracion, tarea))
			else:
				# prioridad basado en el numero de la tarea
				heapq.heappush(self.cola_prioridad, (tarea, duracion, inicio))

		inicio = 0

		trabajos = []

		if opcion == "prioridad_inicio":
			
			# prioridad basado en el inicio de la tarea
			
			for tarea in range(len(self.datos)):
			
				inicio_trab, duracion, tarea = heapq.heappop(self.cola_prioridad)
			
				if inicio <= inicio_trab:
					inicio += duracion  
					trabajos.append(tarea)
		else: 
			
			# prioridad basado en el indice de la tarea
			
			for tarea in range(len(self.datos)):
			
				tarea, duracion, inicio_trab = heapq.heappop(self.cola_prioridad)
			
				if inicio <= inicio_trab:
					inicio = duracion + inicio_trab 
					trabajos.append(tarea)	


		print(trabajos, len(trabajos))

Scheduling_jobs(instancia, "prioridad_inicio")
Scheduling_jobs(instancia, "")