import json
import os

ammo_type_mapping = {
    '5.56x45': 'Ammo_556x45mm',
    '9x18PM': 'Ammo_9x18mm',
    '12ga': 'Ammo_1270',
    '7.62x54R': 'Ammo_762x54mmR',
    '5.45x39': 'Ammo_545x39mm',
    '9x19': 'Ammo_9x19mm',
    '7.62x25': "Ammo_762x25mm",
    '7.62x39': 'Ammo_762x39mm',
    '.366 TKM': 'Ammo_366',
    '9x21': 'Ammo_9x21mm',
    '9x39': 'Ammo_9x39mm',
    '.45 ACP': 'Ammo_45',
    '20ga': 'Ammo_2070',
    '7.62x51': 'Ammo_762x51mm',
    '4.6x30': 'Ammo_4630mm',
    '5.7x28': 'Ammo_5728mm',
    '.300 Blackout': 'Ammo_300',
    '.338 LM': 'Ammo_338',
    '12.7x55': 'Ammo_127x55mm',
    '23x75': 'Ammo_2375mm',
    '40mm': 'Ammo_40mm',
    '6.8x51': 'Ammo_6851mm',
    '26x75': 'Ammo_26x75mm',
    '7.62x54R': 'Ammo_762x54mmR',
    '9x19mm': 'Ammo_9x19mm',
    '.357': 'Ammo_357',
    '20x1': 'Ammo_20x1mm'

}

exclude_names = [
    'RSP-30 reactive signal cartridge (Green)',
    'ROP-30 reactive flare cartridge (White)',
    'RSP-30 reactive signal cartridge (Red)',
    'RSP-30 reactive signal cartridge (Yellow)',
    'ZiD SP-81 26x75 signal pistol'
]

def determine_ammo_type(name):
    for ammo_keyword, table_name in ammo_type_mapping.items():
        if ammo_keyword in name:
            return table_name
    return 'Unknown'

def generate_primary_weapons_sql(json_filepath, output_filepath):
    with open(json_filepath, 'r') as json_file:
        data = json.load(json_file)
    
    sql_statements = []
    for item in data['data']['items']:
        name = item['name'].replace("'", "''")  
        if name in exclude_names:
            continue 
        image = item['image512pxLink']
        ammo_type = determine_ammo_type(name)
        
        sql_statement = f"INSERT INTO PrimaryWeapons (name, image, ammo_type) VALUES ('{name}', '{image}', '{ammo_type}');"
        sql_statements.append(sql_statement)
    
    with open(output_filepath, 'w') as sql_file:
        sql_file.write('\n'.join(sql_statements) + '\n')

if __name__ == "__main__":
    json_filepath = './item_jsons/guns.json'
    output_filepath = './out/guns.sql'
    generate_primary_weapons_sql(json_filepath, output_filepath)
    print(f"SQL statements have been written to {output_filepath}")