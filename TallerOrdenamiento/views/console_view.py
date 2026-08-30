"""
Módulo de Vista para la presentación de resultados en consola.
"""

def display_algorithm_table(algorithm_name: str, results: list[dict]):
    """
    Renderiza una tabla estructurada en consola con los resultados de las pruebas.
    
    Args:
        algorithm_name (str): Nombre del algoritmo evaluado.
        results (list[dict]): Lista de diccionarios que contiene los metadatos
                              (tamaño, tiempo en ns y caso) de cada prueba. # Cambio de ms a ns
    """
    # Se amplía el ancho total de las barras (de 65 a 69) para acomodar los números largos en ns
    print(f"\n{'=' * 69}")
    print(f" TABLA: {algorithm_name.upper()}")
    print(f"{'=' * 69}")
    
    # Se actualiza el título de la columna a 'Tiempo (ns)' y se le da más espacio (<16 en vez de <12)
    print(f"{'Algoritmo':<16} | {'Cantidad de Datos':<18} | {'Tiempo (ns)':<16} | {'Caso':<10}")
    print(f"{'-' * 69}")
    
    for r in results:
        # Se valida como entero (int) porque perf_counter_ns() devuelve enteros.
        # Se usa el formato :, para agregar separadores de miles y facilitar la lectura.
        t = f"{r['time']:,}" if isinstance(r['time'], int) else str(r['time'])
        
        # Se alinea la variable 't' a 16 espacios para que coincida con la nueva cabecera
        print(f"{r['algorithm']:<16} | {r['size']:<18} | {t:<16} | {r['case']:<10}")
        
    print(f"{'-' * 69}")
