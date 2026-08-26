"""
Módulo de persistencia y carga de datos.
"""
import os

def load_dataset(size: int, case: str, base_path: str = "datos_pruebas") -> list[int]:
    """
    Carga en memoria un conjunto de datos desde un archivo de texto.
    
    Args:
        size (int): Cantidad de elementos (ej. 3000, 30000).
        case (str): Tipo de caso ('Mejor', 'Peor', 'Promedio').
        base_path (str, optional): Directorio donde se ubican los archivos.
        
    Returns:
        list[int]: Lista generada a partir de la lectura del archivo.
        
    Raises:
        FileNotFoundError: Si el archivo solicitado no existe en la ruta especificada.
    """
    filename = f"arreglo_{size}_{case.lower()}.txt"
    filepath = os.path.join(base_path, filename)
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")
        
    with open(filepath, "r") as file:
        return [int(line.strip()) for line in file if line.strip()]
        
