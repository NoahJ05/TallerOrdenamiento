"""
Módulo Controlador para la orquestación del Benchmark.
"""
import time
from models.data_loader import load_dataset
from models.sorting_algorithms import bubble_sort, shell_sort, quick_sort, radix_sort, binary_tree_sort
from views.console_view import display_algorithm_table

class BenchmarkController:
    """
    Clase encargada de coordinar la lectura de datos, ejecución de los algoritmos 
    y recolección de los tiempos de cómputo en milisegundos.
    """
    
    def __init__(self):
        self.sizes = [3000, 30000, 300000, 3000000, 30000000]
        self.cases = ["Mejor", "Peor", "Promedio"]
        self.algorithms = {
            "BubbleSort": bubble_sort,
            "ShellSort": shell_sort,
            "QuickSort": quick_sort,
            "RadixSort": radix_sort,
            "BinaryTreeSort": binary_tree_sort
        }

    def execute_benchmarks(self):
        """
        Ejecuta el ciclo de pruebas para todos los algoritmos, tamaños y casos.
        
        Implementa restricciones de seguridad para evitar desbordamientos de memoria 
        o tiempos de ejecución excesivos (congelamientos) en algoritmos de 
        complejidad cuadrática y volúmenes de datos masivos.
        """
        print("Iniciando pruebas de rendimiento con archivos compartidos...\n")

        for algo_name, algo_func in self.algorithms.items():
            results = []
            print(f"> Evaluando {algo_name}...")

            for size in self.sizes:
                # Omitir O(N^2) en N grandes para evitar congelamientos
                if algo_name in ["BubbleSort", "BinaryTreeSort"] and size >= 300000:
                    for case in self.cases:
                        results.append({
                            "algorithm": algo_name,
                            "size": size,
                            "time": "Omitido (> límite)",
                            "case": case
                        })
                    continue
                    
                # Opcional: Limitar ShellSort en la prueba más extrema
                if algo_name == "ShellSort" and size >= 30000000:
                    for case in self.cases:
                        results.append({
                            "algorithm": algo_name,
                            "size": size,
                            "time": "Omitido (> límite)",
                            "case": case
                        })
                    continue

                for case in self.cases:
                    try:
                        print(f"   -> Procesando {algo_name} | N = {size} | Caso: {case}...")
                        data = load_dataset(size, case)
                        
                        start = time.perf_counter()
                        algo_func(data)
                        end = time.perf_counter()

                        elapsed_ms = (end - start) * 1000
                        
                        results.append({
                            "algorithm": algo_name,
                            "size": size,
                            "time": elapsed_ms,
                            "case": case
                        })
                    except FileNotFoundError as err:
                        print(f"Error: {err}")
                        break

            display_algorithm_table(algo_name, results)
