import json
import os

def determine_plate_carrier(name):
    return 'TRUE' if 'plate carrier' in name.lower() else 'FALSE'

def generate_rigs_sql(json_filepath, output_filepath):
    with open(json_filepath, 'r') as json_file:
        data = json.load(json_file)
    
    sql_statements = []
    for item in data['data']['items']:
        name = item['name'].replace("'", "''")  
        image = item['image512pxLink']
        plate_carrier = determine_plate_carrier(name)
        
        sql_statement = f"INSERT INTO Rigs (name, image, plate_carrier) VALUES ('{name}', '{image}', {plate_carrier});"
        sql_statements.append(sql_statement)
    
    with open(output_filepath, 'w') as sql_file:
        sql_file.write('\n'.join(sql_statements) + '\n')

if __name__ == "__main__":
    json_filepath = './item_jsons/rigs.json'  
    output_filepath = './out/rigs.sql' 
    generate_rigs_sql(json_filepath, output_filepath)
    print(f"SQL statements have been written to {output_filepath}")
