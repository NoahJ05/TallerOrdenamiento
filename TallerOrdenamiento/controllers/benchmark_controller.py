import time
from models.data_loader import load_dataset
from models.sorting_algorithms import bubble_sort, shell_sort, quick_sort, radix_sort, binary_tree_sort
from views.console_view import display_algorithm_table


class BenchmarkController:
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
        print("Iniciando pruebas de rendimiento con archivos compartidos...\n")

        for algo_name, algo_func in self.algorithms.items():
            results = []
            print(f"> Evaluando {algo_name}...")

            for size in self.sizes:
                # Omitir O(n^2) en N grandes para evitar congelamientos de horas
                if algo_name in ["BubbleSort", "BinaryTreeSort"] and size >= 300000:
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
                        # 1. Carga previa (no se mide este tiempo)
                        data = load_dataset(size, case)

                        # 2. Medición estricta del algoritmo
                        start = time.perf_counter()
                        algo_func(data)
                        end = time.perf_counter()

                        elapsed = (end - start) * 1000  # <--- Multiplicar por 1000 para obtener milisegundos

                        results.append({
                            "algorithm": algo_name,
                            "size": size,
                            "time": elapsed,
                            "case": case
                        })
                    except FileNotFoundError as err:
                        print(f"Error: {err}")
                        break

            # Mostrar la tabla individual correspondiente a este algoritmo
            display_algorithm_table(algo_name, results)
