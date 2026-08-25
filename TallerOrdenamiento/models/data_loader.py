import os


def load_dataset(size: int, case: str, base_path: str = "datos_pruebas") -> list[int]:
    """Lee el archivo correspondiente a un tamaño y caso específico."""
    filename = f"arreglo_{size}_{case.lower()}.txt"
    filepath = os.path.join(base_path, filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")

    with open(filepath, "r") as file:
        return [int(line.strip()) for line in file if line.strip()]