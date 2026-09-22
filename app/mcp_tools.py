import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "inventory.json")

def search_inventory_mcp(query: str) -> str:
    """
    Herramienta basada en el patrón MCP para recuperar el contexto 
    de datos de inventario a partir de un archivo JSON.
    """
    if not os.path.exists(DATA_PATH):
        return json.dumps({"error": "Archivo de inventario no encontrado."})

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        inventory = json.load(f)

    query_lower = query.lower()
    matches = [
        item for item in inventory
        if query_lower in item["nombre"].lower() or query_lower in item["categoria"].lower()
    ]

    if not matches:
        return json.dumps({"mensaje": f"No se encontraron productos que coincidan con: '{query}'."})

    return json.dumps(matches, ensure_ascii=False, indent=2)