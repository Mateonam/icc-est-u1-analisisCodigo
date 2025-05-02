import benchmarking as bn
from metodos_ordenamiento import MetodosOrdenamiento
if __name__ == "__main__":
    print("Funciona")
    bn.Benchmarking()
    bench = bn.Benchmarking()
    metodosO = MetodosOrdenamiento()

    #tam = 10000
    tamanio = [5000, 10000, 10500]
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