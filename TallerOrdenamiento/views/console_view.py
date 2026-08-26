"""
Módulo de Vista para la presentación de resultados en consola.
"""

def display_algorithm_table(algorithm_name: str, results: list[dict]):
    """
    Renderiza una tabla estructurada en consola con los resultados de las pruebas.
    
    Args:
        algorithm_name (str): Nombre del algoritmo evaluado.
        results (list[dict]): Lista de diccionarios que contiene los metadatos
                              (tamaño, tiempo en ms y caso) de cada prueba.
    """
    print(f"\n{'=' * 65}")
    print(f" TABLA: {algorithm_name.upper()}")
    print(f"{'=' * 65}")
    print(f"{'Algoritmo':<16} | {'Cantidad de Datos':<18} | {'Tiempo (ms)':<12} | {'Caso':<10}")
    print(f"{'-' * 65}")
    for r in results:
        t = f"{r['time']:.4f}" if isinstance(r['time'], float) else str(r['time'])
        print(f"{r['algorithm']:<16} | {r['size']:<18} | {t:<12} | {r['case']:<10}")
    print(f"{'-' * 65}")
