
from pathlib import Path
import re

# Busca datos/productos.txt a partir de donde está este archivo
carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"

lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total_productos = 0
valor_inventario = 0

for linea in lineas[2:]:
    print("-", linea)

    # Extrae el precio de cada producto
    coincidencia = re.search(r"\$\s*([\d.]+)", linea)

    if coincidencia:
        precio = int(coincidencia.group(1).replace(".", ""))
        total_productos += 1
        valor_inventario += precio

print(f"\nTotal de productos: {total_productos}")
print(f"Valor del inventario: ${valor_inventario}")
