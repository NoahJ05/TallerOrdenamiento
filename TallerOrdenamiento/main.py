"""
Módulo principal de la aplicación.

Actúa como punto de entrada para la ejecución del programa. Su responsabilidad
exclusiva es instanciar los componentes de la arquitectura y arrancar el 
proceso de evaluación.
"""

from controllers.benchmark_controller import BenchmarkController

def main():
    """
    Inicializa el controlador del benchmark e invoca el método central 
    que ejecuta las pruebas de rendimiento de los algoritmos.
    """
    controller = BenchmarkController()
    controller.execute_benchmarks()

if __name__ == "__main__":
    main()
