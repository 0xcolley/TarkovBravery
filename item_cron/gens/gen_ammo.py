import json
import os

ammo_types = {
    "Ammo_300": [".300 Blackout", ".300 Whisper"],
    "Ammo_338": [".338 Lapua Magnum"],
    "Ammo_357": [".357 Magnum"],
    "Ammo_366": [".366 TKM"],
    "Ammo_45": [".45 ACP"],
    "Ammo_127x55mm": ["12.7x55mm"],
    "Ammo_1270": ["12/70"],
    "Ammo_2070": ["20/70"],
    "Ammo_20x1mm": ["20x1mm"],
    "Ammo_2375mm": ["23x75mm"],
    "Ammo_4630mm": ["4.6x30mm"],
    "Ammo_40mm": ["40mm"],
    "Ammo_4046mm": ["40x46mm"],
    "Ammo_545x39mm": ["5.45x39mm"],
    "Ammo_5728mm": ["5.7x28mm"],
    "Ammo_6851mm": ["6.8x51mm"],
    "Ammo_762x25mm": ["7.62x25mm"],
    "Ammo_762x39mm": ["7.62x39mm"],
    "Ammo_762x54mmR": ["7.62x54mm R"],
    "Ammo_9x18mm": ["9x18mm"],
    "Ammo_9x19mm": ["9x19mm"],
    "Ammo_9x21mm": ["9x21mm"],
    "Ammo_556x45mm": ["5.56x45mm"],
    "Ammo_9x39mm": ["9x39mm"]
}

def generate_sql_insert(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    sql_statements = []

    for table, keywords in ammo_types.items():
        values = []
        for item in data['data']['items']:
            if any(keyword in item['name'] for keyword in keywords):
                image_link = item.get('image512pxLink', 'placeholder.png')
                values.append(f"('{item['name']}', '{image_link}')")
        
        if values:
            sql_insert = f"INSERT INTO {table} (name, image) VALUES\n" + ",\n".join(values) + ";"
            sql_statements.append(sql_insert)
    
    return sql_statements

def write_sql_to_file(sql_statements, output_file_path):
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    with open(output_file_path, 'w') as file:
        for statement in sql_insert_statements:
            file.write(statement + '\n' + '\n')

json_file_path = './item_jsons/ammo.json'
output_file_path = './out/ammo.sql'
sql_insert_statements = generate_sql_insert(json_file_path)

write_sql_to_file(sql_insert_statements, output_file_path)

print(f"{output_file_path}")
