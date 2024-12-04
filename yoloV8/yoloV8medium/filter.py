import json

# Leer el archivo JSON generado
with open('runs/detect/val/predictions.json', 'r') as f:
    data = json.load(f)

# Filtrar resultados solo para la clase deseada
filtered_data = [item for item in data if item['category_id'] == 0]

# Guardar el JSON filtrado
with open('persons_results.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)