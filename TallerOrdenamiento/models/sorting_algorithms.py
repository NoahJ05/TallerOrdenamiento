"""
Módulo de Algoritmos de Ordenamiento.

Contiene las implementaciones de 5 algoritmos clásicos ajustados para ordenar 
listas de enteros en orden DESCENDENTE.

Autor: Johan Mauricio Orozco Garcia
"""

import sys
sys.setrecursionlimit(2000000)

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista utilizando el algoritmo de Burbuja (Bubble Sort).
    
    Implementa una bandera 'swapped' para optimizar el Mejor Caso.
    
    Args:
        arr (list[int]): Lista de enteros a ordenar.
        
    Returns:
        list[int]: Lista ordenada en formato descendente.
        
    Complejidad:
        - Mejor caso: O(N) (Arreglo ya ordenado)
        - Promedio / Peor caso: O(N^2)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def shell_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista utilizando el algoritmo Shell Sort.
    
    Utiliza la secuencia de brechas original de Shell (N/2).
    
    Args:
        arr (list[int]): Lista de enteros a ordenar.
        
    Returns:
        list[int]: Lista ordenada en formato descendente.
        
    Complejidad:
        - Promedio: Depende de la brecha, aprox. O(N^1.3) a O(N log^2 N)
        - Peor caso: O(N^2)
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quick_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista utilizando Quick Sort in-place.
    
    Utiliza el elemento central como pivote para evitar la degradación 
    a complejidad cuadrática en listas previamente ordenadas.
    
    Args:
        arr (list[int]): Lista de enteros a ordenar.
        
    Returns:
        list[int]: Lista ordenada en formato descendente.
        
    Complejidad:
        - Mejor / Promedio: O(N log N)
        - Peor caso: O(N log N) (Protegido por el pivote central)
    """
    def _quicksort(items, low, high):
        if low < high:
            p = _partition(items, low, high)
            _quicksort(items, low, p - 1)
            _quicksort(items, p + 1, high)

    def _partition(items, low, high):
        mid = (low + high) // 2
        items[mid], items[high] = items[high], items[mid]
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] >= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quicksort(arr, 0, len(arr) - 1)
    return arr

def radix_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista utilizando Radix Sort basado en Counting Sort.
    
    El proceso de conteo y acumulación está invertido para lograr
    el orden descendente.
    
    Args:
        arr (list[int]): Lista de enteros positivos.
        
    Returns:
        list[int]: Lista ordenada en formato descendente.
        
    Complejidad:
        - Todos los casos: O(N * d) donde d es la cantidad de dígitos.
    """
    def _counting_sort_desc(arr_in, exp):
        n = len(arr_in)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (arr_in[i] // exp) % 10
            count[index] += 1
        for i in range(8, -1, -1):
            count[i] += count[i + 1]
        for i in range(n - 1, -1, -1):
            index = (arr_in[i] // exp) % 10
            output[count[index] - 1] = arr_in[i]
            count[index] -= 1
        for i in range(n):
            arr_in[i] = output[i]

    if not arr:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_desc(arr, exp)
        exp *= 10
    return arr

class TreeNode:
    """Nodo fundamental para la estructura del Árbol Binario de Búsqueda."""
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

def binary_tree_sort(arr: list[int]) -> list[int]:
    """
    Ordena una lista insertando sus elementos en un Árbol Binario de Búsqueda.
    
    Se implementa de forma iterativa tanto la inserción como el recorrido
    (Derecha-Raíz-Izquierda) para evitar desbordamientos de pila (RecursionError)
    ante árboles degenerados.
    
    Args:
        arr (list[int]): Lista de enteros a ordenar.
        
    Returns:
        list[int]: Lista extraída del árbol en orden descendente.
        
    Complejidad:
        - Mejor / Promedio: O(N log N)
        - Peor caso: O(N^2) (Árbol degenerado como lista enlazada)
    """
    if not arr:
        return []
    
    root = TreeNode(arr[0])
    for val in arr[1:]:
        curr = root
        while True:
            if val <= curr.key:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

    result = []
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right
        curr = stack.pop()
        result.append(curr.key)
        curr = curr.left

    return result
    return result
