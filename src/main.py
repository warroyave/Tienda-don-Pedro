from pathlib import Path

# Busca datos/productos.txt a partir de donde está este archivo,
# así funciona desde cualquier carpeta (terminal o botón ▶ de VS Code)
carpeta_proyecto = Path(__file__).parent.parent
archivo = carpeta_proyecto / "datos" / "productos.txt"
lineas = archivo.read_text(encoding="utf-8").splitlines()
print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)