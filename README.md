# Taller de Algoritmos de Ordenamiento

**Universidad Distrital Francisco José de Caldas**  
**Estudiante:** Johan Mauricio Orozco García

Este repositorio contiene la implementación, ejecución y evaluación empírica de cinco algoritmos de ordenamiento clásicos. El proyecto está dividido en dos módulos desarrollados en Java y Python.

## Algoritmos Implementados (Orden Descendente)
1. **BubbleSort**
2. **ShellSort**
3. **QuickSort** (In-place con pivote central)
4. **RadixSort** (Basado en base 10)
5. **Binary Tree Sort** (Iterativo)

## Arquitectura del Proyecto

El código fuente está modularizado utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)**.

*   `TallerOrdenamientoGenerador/` (Java/Eclipse): Contiene la clase `Generador15Casos.java` responsable de crear los arreglos predefinidos (semilla controlada) para el Mejor, Peor y Caso Promedio en tamaños de N = 3.000 hasta N = 30.000.000.
*   `TallerOrdenamiento/` (Python/PyCharm):
    *   **Models:** Lógica matemática de los algoritmos e ingesta de datos a RAM.
    *   **Views:** Interfaz de consola para renderizar las métricas.
    *   **Controllers:** Orquestación y medición de tiempos (`time.perf_counter` transformado a milisegundos).

## Instrucciones de Uso

1.  **Generación de Datos:** Ejecutar la clase Java `Generador15Casos` para construir el directorio `datos_pruebas/`.
2.  **Integración:** Trasladar la carpeta `datos_pruebas/` a la raíz del entorno de Python. *(Nota: Esta carpeta está excluida del repositorio mediante `.gitignore` debido a que excede los límites de tamaño en GitHub).*
3.  **Ejecución:** Correr el archivo `main.py` para visualizar las tablas de tiempos de ejecución por cada algoritmo.

> **Aviso de Rendimiento:** Las métricas correspondientes a algoritmos de complejidad asintótica O(N^2) (BubbleSort y BinaryTreeSort degenerado) para tamaños de N >= 300.000 son omitidas automáticamente por el controlador para prevenir el desbordamiento de memoria o esperas estimadas en múltiples días de procesamiento.
