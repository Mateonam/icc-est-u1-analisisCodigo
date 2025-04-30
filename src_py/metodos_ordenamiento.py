class MetodosOrdenamiento:
    def bubble_sort(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1, n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i] , arreglo[j] = arreglo[j] , arreglo[i]
        return arreglo
    
    def improved_bubble_sort(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            intercambio = False
            for j in range(0, n - 1 -i):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
                intercambio = True
                if not intercambio:
                    break
        return arreglo
        


    def selection_sort(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(0, n - 1):
            min = i
            for j in range(i + 1, n):
                if arreglo[i] < arreglo[min]:
                    min = j
            arreglo[min] , arreglo[i] = arreglo[i] , arreglo[min]
        return arreglo
    