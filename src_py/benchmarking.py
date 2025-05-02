from metodos_ordenamiento import MetodosOrdenamiento
import random
import time
class Benchmarking:

    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio

    # def __init__(self):
       # print("Benchmarking instanciado")
        # self.mO = MetodosOrdenamiento()
        # arreglo = self.build_arreglo(10000)
        # tarea = lambda: self.mO.bubble_sort(arreglo)
        # tarea2 = lambda: self.mO.improved_bubble_sort(arreglo)
        # tarea3 = lambda: self.mO.selection_sort(arreglo)
        
        # time_milis = self.contar_con_current_time_milles(tarea)
        # time_milis2 = self.contar_con_current_time_milles(tarea2)
        # time_milis3 = self.contar_con_current_time_milles(tarea3)
        # time_ns = self.contar_con_nano_time(tarea)
        # time_ns2 = self.contar_con_nano_time(tarea2)
        # time_ns3 = self.contar_con_nano_time(tarea3)


        # print(f"tiempo en mls: {time_milis}")
        # print(f"tiempo en ns: {time_ns}")
        # print(f"tiempo en mls: {time_milis2}")
        # print(f"tiempo en ns: {time_ns2}")
        # print(f"tiempo en mls: {time_milis3}")
        # print(f"tiempo en ns: {time_ns3}")

    def build_arreglo(self, tamano):
        arreglo = []
        for _ in range(tamano):
            numero = random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo

    def contar_con_current_time_milles(self, tarea):
        x = time.time()
        tarea()
        f = time.time_ns()
        return f - x

    def contar_con_nano_time(self, tarea):
        inicio = time.time_ns()
        tarea()
        fin = time.time_ns()
        return (fin - inicio) / 1_000_000_000.0