import matplotlib.pyplot as plt
import benchmarking as bn
from metodos_ordenamiento import MetodosOrdenamiento
from datetime import datetime

if __name__ == "__main__":
    print("Funciona")
    bn.Benchmarking()
    bench = bn.Benchmarking()
    metodosO = MetodosOrdenamiento()

    #tam = 10000
    tamanio = [0, 1000, 2000]
    resultados = []
    for tam in tamanio:
        arreglo_base = bench.build_arreglo(tam)
        metodos_dic = {
            "Burbuja" : metodosO.bubble_sort,
            "Buebuja mejorado" : metodosO.improved_bubble_sort,
            "Selección" : metodosO.selection_sort,
            "Shell" : metodosO.shell_sort
        }

    
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_resultado = bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_resultado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre del método: {nombre}, tiempo: {tiempo:.6f} segundos")

    #Preparar datos para ser graficados
    #1. crear un diccionario o map para almacenar resultados por métodos
    tiempos_by_metodos = {
         "Burbuja" : [],
            "Buebuja mejorado" : [],
            "Selección" : [],
            "Shell" : []
    }
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodos[nombre].append(tiempo)


# Crear la figura y guardar en la variable 'fig'
# Obtener fecha y hora actual solo una vez
fecha_hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Subtítulos personalizados para cada gráfico
subtitulo_1 = "Comparación de Tiempos de Ejecución de Algoritmos de Ordenamiento"
subtitulo_2 = "Gráfico de Ejemplo con Matplotlib"

# Crear figura con 1 fila y 2 columnas
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Cambiar el título de la ventana
fig.canvas.manager.set_window_title(f"Mateo Namicela - {fecha_hora_actual}")

# Título general arriba y centrado
fig.suptitle(f"Mateo Namicela - {fecha_hora_actual}", fontsize=14)

# === Primer gráfico ===
for nombre, tiempos in tiempos_by_metodos.items():
    axs[0].plot(tamanio, tiempos, label=nombre, marker="o")

axs[0].set_title(subtitulo_1)
axs[0].set_xlabel("Tamaño de los arreglos")
axs[0].set_ylabel("Tiempo de ejecución (s)")
axs[0].legend()

# === Segundo gráfico ===
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

axs[1].plot(x, y, label="Línea", color="blue")
axs[1].set_title(subtitulo_2)
axs[1].set_xlabel("Eje de la x")
axs[1].set_ylabel("Eje de la y")
axs[1].legend()

# Ajustar espaciado
plt.tight_layout(rect=[0, 0, 1, 0.95])  # deja espacio para el suptítulo

# Mostrar gráfica
plt.show()
