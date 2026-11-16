import sqlite3
import json
import csv
import xml.etree.ElementTree as ET
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "shelter.db"
OUT_DIR = BASE_DIR / "out"

OUT_DIR.mkdir(exist_ok=True)

connection = sqlite3.connect(DB_PATH)
connection.row_factory = sqlite3.Row

query = """
SELECT
    animals.animal_id,
    animals.name,
    animals.species,
    animals.age,
    adoptions.adoption_id,
    adoptions.adoption_date
FROM animals
LEFT JOIN adoptions ON animals.animal_id = adoptions.animal_id
"""

rows = connection.execute(query).fetchall()
connection.close()

data = []

for row in rows:
    animal = {
        "animal_id": row["animal_id"],
        "name": row["name"],
        "species": row["species"],
        "age": row["age"],
        "adoption": None
    }

    if row["adoption_id"] is not None:
        animal["adoption"] = {
            "adoption_id": row["adoption_id"],
            "adoption_date": row["adoption_date"]
        }

    data.append(animal)

with open(OUT_DIR / "data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

csv_data = []

for animal in data:
    adoption = animal["adoption"] or {}

    csv_data.append({
        "animal_id": animal["animal_id"],
        "name": animal["name"],
        "species": animal["species"],
        "age": animal["age"],
        "adoption_id": adoption.get("adoption_id"),
        "adoption_date": adoption.get("adoption_date")
    })

with open(OUT_DIR / "data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=csv_data[0].keys())
    writer.writeheader()
    writer.writerows(csv_data)

root = ET.Element("animals")

for animal in data:
    animal_element = ET.SubElement(root, "animal")

    for key in ["animal_id", "name", "species", "age"]:
        ET.SubElement(animal_element, key).text = str(animal[key])

    adoption_element = ET.SubElement(animal_element, "adoption")

    if animal["adoption"] is not None:
        for key, value in animal["adoption"].items():
            ET.SubElement(adoption_element, key).text = str(value)

tree = ET.ElementTree(root)
ET.indent(tree, space="    ")
tree.write(OUT_DIR / "data.xml", encoding="utf-8", xml_declaration=True)

with open(OUT_DIR / "data.yaml", "w", encoding="utf-8") as file:
    yaml.dump(data, file, allow_unicode=True, sort_keys=False)

print("Все четыре файла успешно созданы!")